// @ts-check

import { $el } from "../../ui.js";
import { QuasarButton } from "./button.js";
import { prop } from "../../utils.js";

export class QuasarButtonGroup {
	element = $el("div.quasarui-button-group");

	/** @param {Array<QuasarButton | HTMLElement>} buttons */
	constructor(...buttons) {
		this.buttons = prop(this, "buttons", buttons, () => this.update());
	}

	/**
	 * @param {QuasarButton} button
	 * @param {number} index
	 */
	insert(button, index) {
		this.buttons.splice(index, 0, button);
		this.update();
	}

	/** @param {QuasarButton} button */
	append(button) {
		this.buttons.push(button);
		this.update();
	}

	/** @param {QuasarButton|number} indexOrButton */
	remove(indexOrButton) {
		if (typeof indexOrButton !== "number") {
			indexOrButton = this.buttons.indexOf(indexOrButton);
		}
		if (indexOrButton > -1) {
			const r = this.buttons.splice(indexOrButton, 1);
			this.update();
			return r;
		}
	}

	update() {
		this.element.replaceChildren(...this.buttons.map((b) => b["element"] ?? b));
	}
}
