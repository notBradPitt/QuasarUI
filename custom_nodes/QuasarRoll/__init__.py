from .Quasarroll_Nodes import *
from .Quasarroll_Pipe_Nodes import *
from .Quasarroll_SDXL_Nodes import *
from .upscale import *

NODE_CLASS_MAPPINGS = {
    "CR Image Input Switch": Quasarroll_ImageInputSwitch,
    "CR Image Input Switch (4 way)": Quasarroll_ImageInputSwitch_4way,
    "CR Latent Input Switch": Quasarroll_LatentInputSwitch,
    "CR Conditioning Input Switch": Quasarroll_ConditioningInputSwitch,
    "CR Clip Input Switch": Quasarroll_ClipInputSwitch,
    "CR Model Input Switch": Quasarroll_ModelInputSwitch,
    "CR ControlNet Input Switch": Quasarroll_ControlNetInputSwitch,
    "CR Text Input Switch": Quasarroll_TextInputSwitch,
    "CR Text Input Switch (4 way)": Quasarroll_TextInputSwitch_4way,
    "CR Switch Model and CLIP":Quasarroll_ModelAndCLIPInputSwitch,
    "CR Load LoRA": Quasarroll_LoraLoader,
    "CR Apply ControlNet": Quasarroll_ApplyControlNet,
    "CR Image Size": Quasarroll_ImageSize_Float,
    "CR Image Output": Quasarroll_ImageOutput,
    "CR Integer Multiple": Quasarroll_Int_Multiple_Of,
    "CR Aspect Ratio": Quasarroll_AspectRatio,
    "CR Seed to Int": Quasarroll_SeedToInt,
    "CR Integer To String":CR_IntegerToString,
    "CR Float To String":CR_FloatToString,
    "CR Color Tint": Quasarroll_Color_Tint,
    "CR Img2Img Process Switch": Quasarroll_InputLatentsText,
    "CR Hires Fix Process Switch": Quasarroll_HiResFixSwitch,
    "CR Halftone Grid" : Quasarroll_Halftone_Grid,
    "CR Latent Batch Size": Quasarroll_LatentBatchSize,
    "CR LoRA Stack":Quasarroll_LoRA_Stack,
    "CR Apply LoRA Stack":Quasarroll_ApplyLoRA_Stack,    
    "CR SD1.5 Aspect Ratio":Quasarroll_AspectRatio_v2,
    "CR Batch Process Switch": Quasarroll_BatchProcessSwitch,
    "CR Multi-ControlNet Stack":Quasarroll_ControlNetStack,
    "CR Apply Multi-ControlNet":Quasarroll_ApplyControlNetStack,    
    "CR Seed": Quasarroll_Seed,
    "CR Apply Model Merge":Quasarroll_ApplyModelMerge,
    "CR Model Merge Stack":Quasarroll_ModelMergeStack,
    ### Pipe Nodes
    "CR Module Pipe Loader": CR_module_pipe_loader,
    "CR Module Input": CR_module_input,
    "CR Module Output": CR_module_output,
    "CR Image Pipe In": CR_image_pipe_in,
    "CR Image Pipe Edit": CR_image_pipe_edit,
    "CR Image Pipe Out": CR_image_pipe_out,
    "CR Pipe Switch": CR_input_switch_pipe,
    ### SDXL Nodes
    "CR SDXL Prompt Mix Presets": Quasarroll_prompt_mixer_v2,
    "CR SDXL Aspect Ratio":Quasarroll_SDXL_AspectRatio_v2,
    "CR SDXL Prompt Mixer": Quasarroll_prompt_mixer,
    "CR SDXL Style Text": Quasarroll_SDXLStyleText,
    "CR SDXL Base Prompt Encoder": Quasarroll_SDXLBasePromptEncoder, 
    "CR Aspect Ratio SDXL": Quasarroll_AspectRatio_SDXL,
    ### Upscale Nodes
    "CR Multi Upscale Stack":CR_MultiUpscaleStack,
    "CR Upscale Image":CR_UpscaleImage,
    "CR Apply Multi Upscale":CR_ApplyMultiUpscale,
}

__all__ = ['NODE_CLASS_MAPPINGS']

print("\033[34mQuasarroll Custom Nodes: \033[92mLoaded\033[0m")
