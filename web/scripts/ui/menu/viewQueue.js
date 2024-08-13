// @ts-check

import { QuasarButton } from "../components/button.js";
import { QuasarViewList, QuasarViewListButton } from "./viewList.js";
import { api } from "../../api.js";

export class QuasarViewQueueButton extends QuasarViewListButton {
	constructor(app) {
		super(app, {
			button: new QuasarButton({
				content: "View Queue",
				icon: "format-list-numbered",
				tooltip: "View queue",
				classList: "quasarui-button quasarui-queue-button",
			}),
			list: QuasarViewQueueList,
			mode: "Queue",
		});
	}
}

export class QuasarViewQueueList extends QuasarViewList {
	getRow = (item, section) => {
		if (section !== "Running") {
			return super.getRow(item, section);
		}
		return {
			text: item.prompt[0] + "",
			actions: [
				{
					text: "Load",
					action: async () => {
						try {
							await this.app.loadGraphData(item.prompt[3].extra_pnginfo.workflow);
							if (item.outputs) {
								this.app.nodeOutputs = item.outputs;
							}
						} catch (error) {
							alert("Error loading workflow: " + error.message);
							console.error(error);
						}
					},
				},
				{
					text: "Cancel",
					action: async () => {
						try {
							await api.interrupt();
						} catch (error) {}
					},
				},
			],
		};
	}
}
