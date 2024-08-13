// @ts-check

import { $el } from "../../ui.js";
import { QuasarButton } from "./button.js";
import { prop } from "../../utils.js";
import { QuasarPopup } from "./popup.js";

export class QuasarSplitButton {
	/**
	 *  @param {{
	 * 		primary: QuasarButton,
	 * 		mode?: "hover" | "click",
	 * 		horizontal?: "left" | "right",
	 * 		position?: "relative" | "absolute"
	 *  }} param0
	 *  @param {Array<QuasarButton> | Array<HTMLElement>} items
	 */
	constructor({ primary, mode, horizontal = "left", position = "relative" }, ...items) {
		this.arrow = new QuasarButton({
			icon: "chevron-down",
		});
		this.element = $el("div.quasarui-split-button" + (mode === "hover" ? ".hover" : ""), [
			$el("div.quasarui-split-primary", primary.element),
			$el("div.quasarui-split-arrow", this.arrow.element),
		]);
		this.popup = new QuasarPopup({
			target: this.element,
			container: position === "relative" ? this.element : document.body,
			classList: "quasarui-split-button-popup" + (mode === "hover" ? " hover" : ""),
			closeOnEscape: mode === "click",
			position,
			horizontal,
		});

		this.arrow.withPopup(this.popup, mode);

		this.items = prop(this, "items", items, () => this.update());
	}

	update() {
		this.popup.element.replaceChildren(...this.items.map((b) => b.element ?? b));
	}
}
