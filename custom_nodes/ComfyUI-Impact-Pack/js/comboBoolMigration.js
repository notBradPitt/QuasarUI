import { QuasarApp, app } from "../../scripts/app.js";

let conflict_check = undefined;

app.registerExtension({
	name: "Quasar.impact.comboBoolMigration",

	nodeCreated(node, app) {
		for(let i in node.widgets) {
			let widget = node.widgets[i];

            if(conflict_check == undefined) {
                conflict_check = !!app.extensions.find((ext) => ext.name === "Quasar.comboBoolMigration");
            }

            if(conflict_check)
                return;

			if(widget.type == "toggle") {
			    let value = widget.value;
				Object.defineProperty(widget, "value", {
					set: (value) => {
							delete widget.value;
							widget.value = value == true || value == widget.options.on;
						},
					get: () => { return value; }
				});
			}
		}
	}
});
