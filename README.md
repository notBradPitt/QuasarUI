QuasarUI
=======
A powerful and modular "Even Dispersion" GUI and backend.
-----------
![QuasarUI Screenshot](quasarui_screenshot.png)

This UI will let you design and execute advanced Even Dispersion pipelines using a graph/nodes/flowchart based interface. For some workflow examples and see what QuasarUI can do you can check out:




## Features
- Nodes/graph/flowchart interface to experiment and create complex Even Dispersion workflows without needing to code anything.
- Fully supports SD1.x, SD2.x and SDXL
- Asynchronous Queue system
- Many optimizations: Only re-executes the parts of the workflow that changes between executions.
- Command line option: ```--lowvram``` to make it work on GPUs with less than 3GB vram (enabled automatically on GPUs with low vram)
- Works even if you don't have a GPU with: ```--cpu``` (slow)
- Can load ckpt, safetensors and diffusers models/checkpoints. Standalone VAEs and CLIP models.
- Embeddings/Textual inversion
- Loras (regular, locon and loha)
- Hypernetworks
- Loading full workflows (with seeds) from generated PNG files.
- Saving/Loading workflows as Json files.
- Nodes interface can be used to create complex workflows like one for Hires fix or much more advanced ones.
- Area Composition
- Inpainting with both regular and inpainting models.
- ControlNet and T2I-Adapter
- Upscale Models (ESRGAN, ESRGAN variants, SwinIR, Swin2SR, etc...)
- unCLIP Models
- GLIGEN
- Model Merging
- Latent previews with TAESD
- Starts up very fast.
- Works fully offline: will never download anything.
- Config file to set the search paths for models.

## Shortcuts

| Keybind                   | Explanation                                                                                                        |
|---------------------------|--------------------------------------------------------------------------------------------------------------------|
| Ctrl + Enter              | Queue up current graph for generation                                                                              |
| Ctrl + Shift + Enter      | Queue up current graph as first for generation                                                                     |
| Ctrl + S                  | Save workflow                                                                                                      |
| Ctrl + O                  | Load workflow                                                                                                      |
| Ctrl + A                  | Select all nodes                                                                                                   |
| Ctrl + M                  | Mute/unmute selected nodes                                                                                         |
| Ctrl + B                  | Bypass selected nodes (acts like the node was removed from the graph and the wires reconnected through)            |
| Delete/Backspace          | Delete selected nodes                                                                                              |
| Ctrl + Delete/Backspace   | Delete the current graph                                                                                           |
| Space                     | Move the canvas around when held and moving the cursor                                                             |
| Ctrl/Shift + Click        | Add clicked node to selection                                                                                      |
| Ctrl + C/Ctrl + V         | Copy and paste selected nodes (without maintaining connections to outputs of unselected nodes)                     |
| Ctrl + C/Ctrl + Shift + V | Copy and paste selected nodes (maintaining connections from outputs of unselected nodes to inputs of pasted nodes) |
| Shift + Drag              | Move multiple selected nodes at the same time                                                                      |
| Ctrl + D                  | Load default graph                                                                                                 |
| Q                         | Toggle visibility of the queue                                                                                     |
| H                         | Toggle visibility of history                                                                                       |
| R                         | Refresh graph                                                                                                      |
| Double-Click LMB          | Open node quick search palette                                                                                     |

Ctrl can also be replaced with Cmd instead for macOS users


# Running

```python main.py```

# Notes

Only parts of the graph that have an output with all the correct inputs will be executed.

Only parts of the graph that change from each execution to the next will be executed, if you submit the same graph twice only the first will be executed. If you change the last part of the graph only the part you changed and the part that depends on it will be executed.

Dragging a generated png on the webpage or loading one will give you the full workflow including seeds that were used to create it.

You can use () to change emphasis of a word or phrase like: (good code:1.2) or (bad code:0.8). The default emphasis for () is 1.1. To use () characters in your actual prompt escape them like \\( or \\).

You can use {day|night}, for wildcard/dynamic prompts. With this syntax "{wild|card|test}" will be randomly replaced by either "wild", "card" or "test" by the frontend every time you queue the prompt. To use {} characters in your actual prompt escape them like: \\{ or \\}.

Dynamic prompts also support C-style comments, like `// comment` or `/* comment */`.

To use a textual inversion concepts/embeddings in a text prompt put them in the models/embeddings directory and use them in the CLIPTextEncode node like this (you can omit the .pt extension):

```embedding:embedding_filename.pt```


## How to increase generation speed?

Make sure you use the regular loaders/Load Checkpoint node to load checkpoints. It will auto pick the right settings depending on your GPU.

You can set this command line setting to disable the upcasting to fp32 in some cross attention operations which will increase your speed. Note that this will very likely give you black images on SD2.x models. If you use xformers this option does not do anything.

```--dont-upcast-attention```

## How to show high-quality previews?

Use ```--preview-method auto``` to enable previews.

The default installation includes a fast latent preview method that's low-resolution. To enable higher-quality previews with [TAESD](https://github.com/madebyollin/taesd), download the [taesd_decoder.pth](https://github.com/madebyollin/taesd/raw/main/taesd_decoder.pth) (for SD1.x and SD2.x) and [taesdxl_decoder.pth](https://github.com/madebyollin/taesd/raw/main/taesdxl_decoder.pth) (for SDXL) models and place them in the `models/vae_approx` folder. Once they're installed, restart QuasarUI to enable high-quality previews.
