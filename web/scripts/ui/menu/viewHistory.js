// @ts-check

import { QuasarButton } from "../components/button.js";
import { QuasarViewList, QuasarViewListButton } from "./viewList.js";

export class QuasarViewHistoryButton extends QuasarViewListButton {
	constructor(app) {
		super(app, {
			button: new QuasarButton({
				content: "View History",
				icon: "history",
				tooltip: "View history",
				classList: "quasarui-button quasarui-history-button",
			}),
			list: QuasarViewHistoryList,
			mode: "History",
		});
	}
}

export class QuasarViewHistoryList extends QuasarViewList {
	async loadItems() {
		const items = await super.loadItems();
		items["History"].reverse();
		return items;
	}
}
