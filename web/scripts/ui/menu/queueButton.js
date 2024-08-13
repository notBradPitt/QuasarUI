// @ts-check

import { QuasarButton } from "../components/button.js";
import { $el } from "../../ui.js";
import { api } from "../../api.js";
import { QuasarSplitButton } from "../components/splitButton.js";
import { QuasarQueueOptions } from "./queueOptions.js";
import { prop } from "../../utils.js";

export class QuasarQueueButton {
	element = $el("div.quasarui-queue-button");
	#internalQueueSize = 0;

	queuePrompt = async (e) => {
		this.#internalQueueSize += this.queueOptions.batchCount;
		// Hold shift to queue front, event is undefined when auto-queue is enabled
		await this.app.queuePrompt(e?.shiftKey ? -1 : 0, this.queueOptions.batchCount);
	};

	constructor(app) {
		this.app = app;
		this.queueSizeElement = $el("span.quasarui-queue-count", {
			textContent: "?",
		});

		const queue = new QuasarButton({
			content: $el("div", [
				$el("span", {
					textContent: "Queue",
				}),
				this.queueSizeElement,
			]),
			icon: "play",
			classList: "quasarui-button",
			action: this.queuePrompt,
		});

		this.queueOptions = new QuasarQueueOptions(app);

		const btn = new QuasarSplitButton(
			{
				primary: queue,
				mode: "click",
				position: "absolute",
				horizontal: "right",
			},
			this.queueOptions.element
		);
		btn.element.classList.add("primary");
		this.element.append(btn.element);

		this.autoQueueMode = prop(this, "autoQueueMode", "", () => {
			switch (this.autoQueueMode) {
				case "instant":
					queue.icon = "infinity";
					break;
				case "change":
					queue.icon = "auto-mode";
					break;
				default:
					queue.icon = "play";
					break;
			}
		});

		this.queueOptions.addEventListener("autoQueueMode", (e) => (this.autoQueueMode = e["detail"]));

		api.addEventListener("graphChanged", () => {
			if (this.autoQueueMode === "change") {
				if (this.#internalQueueSize) {
					this.graphHasChanged = true;
				} else {
					this.graphHasChanged = false;
					this.queuePrompt();
				}
			}
		});

		api.addEventListener("status", ({ detail }) => {
			this.#internalQueueSize = detail?.exec_info?.queue_remaining;
			if (this.#internalQueueSize != null) {
				this.queueSizeElement.textContent = this.#internalQueueSize > 99 ? "99+" : this.#internalQueueSize + "";
				this.queueSizeElement.title = `${this.#internalQueueSize} prompts in queue`;
				if (!this.#internalQueueSize && !app.lastExecutionError) {
					if (this.autoQueueMode === "instant" || (this.autoQueueMode === "change" && this.graphHasChanged)) {
						this.graphHasChanged = false;
						this.queuePrompt();
					}
				}
			}
		});
	}
}
