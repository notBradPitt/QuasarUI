// @ts-check

import { api } from "../../api.js";
import { QuasarButton } from "../components/button.js";

export function getInteruptButton(visibility) {
	const btn = new QuasarButton({
		icon: "close",
		tooltip: "Cancel current generation",
		enabled: false,
		action: () => {
			api.interrupt();
		},
		classList: ["quasarui-button", "quasarui-interrupt-button", visibility],
	});

	api.addEventListener("status", ({ detail }) => {
		const sz = detail?.exec_info?.queue_remaining;
		btn.enabled = sz > 0;
	});

	return btn;
}
