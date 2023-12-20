import gradio as gr

from dreambooth.utils.ui_utils import ElementManager

manager = ElementManager()

GRADIENT_ACCUMULATION_STEPS = None
TRAIN_BATCH_SIZE = None
CAPTION_COLUMN = None
DATASET_CONFIG_NAME = None
DATASET_NAME = None
IMAGE_COLUMN = None
TRAIN_DATA_DIR = None
CENTER_CROP = None
RANDOM_FLIP = None
RESOLUTION = None
CHECKPOINTING_STEPS = None
MAX_TRAIN_SAMPLES = None
MAX_TRAIN_STEPS = None
NUM_TRAIN_EPOCHS = None
VALIDATION_EPOCHS = None
RANK = None
LEARNING_RATE = None
LR_SCHEDULER = None
LR_WARMUP_STEPS = None
SCALE_LR = None
LOGGING_DIR = None
REPORT_TO = None
ADAM_BETA1 = None
ADAM_BETA2 = None
ADAM_EPSILON = None
ADAM_WEIGHT_DECAY = None
MAX_GRAD_NORM = None
ALLOW_TF32 = None
DATALOADER_NUM_WORKERS = None
ENABLE_XFORMERS_MEMORY_EFFICIENT_ATTENTION = None
GRADIENT_CHECKPOINTING = None
LOCAL_RANK = None
MIXED_PRECISION = None
NOISE_OFFSET = None
PREDICTION_TYPE = None
SEED = None
SNR_GAMMA = None
USE_8BIT_ADAM = None
CHECKPOINTS_TOTAL_LIMIT = None
HUB_MODEL_ID = None
HUB_TOKEN = None
PUSH_TO_HUB = None
NUM_VALIDATION_IMAGES = None
VALIDATION_PROMPT = None


def render():
    global GRADIENT_ACCUMULATION_STEPS
    global TRAIN_BATCH_SIZE
    global CAPTION_COLUMN
    global DATASET_CONFIG_NAME
    global DATASET_NAME
    global IMAGE_COLUMN
    global TRAIN_DATA_DIR
    global CENTER_CROP
    global RANDOM_FLIP
    global RESOLUTION
    global CHECKPOINTING_STEPS
    global MAX_TRAIN_SAMPLES
    global MAX_TRAIN_STEPS
    global NUM_TRAIN_EPOCHS
    global VALIDATION_EPOCHS
    global RANK
    global LEARNING_RATE
    global LR_SCHEDULER
    global LR_WARMUP_STEPS
    global SCALE_LR
    global LOGGING_DIR
    global REPORT_TO
    global ADAM_BETA1
    global ADAM_BETA2
    global ADAM_EPSILON
    global ADAM_WEIGHT_DECAY
    global MAX_GRAD_NORM
    global ALLOW_TF32
    global DATALOADER_NUM_WORKERS
    global ENABLE_XFORMERS_MEMORY_EFFICIENT_ATTENTION
    global GRADIENT_CHECKPOINTING
    global LOCAL_RANK
    global MIXED_PRECISION
    global NOISE_OFFSET
    global PREDICTION_TYPE
    global SEED
    global SNR_GAMMA
    global USE_8BIT_ADAM
    global CHECKPOINTS_TOTAL_LIMIT
    global HUB_MODEL_ID
    global HUB_TOKEN
    global PUSH_TO_HUB
    global NUM_VALIDATION_IMAGES
    global VALIDATION_PROMPT
    with gr.Accordion(open=False, label="Batching") as BATCHING_ACCORDION:
        GRADIENT_ACCUMULATION_STEPS = gr.Slider(label='Gradient Accumulation Steps', value=1, visible=True, step=1, minimum=0, maximum=100)
        TRAIN_BATCH_SIZE = gr.Slider(label='Train Batch Size', value=4, visible=True, step=1, minimum=1, maximum=1000)
    with gr.Accordion(open=False, label="Dataset") as DATASET_ACCORDION:
        CAPTION_COLUMN = gr.Textbox(label='Caption Column', value='text', visible=True)
        DATASET_CONFIG_NAME = gr.Textbox(label='Dataset Config Name', value='None', visible=True)
        DATASET_NAME = gr.Textbox(label='Dataset Name', value='None', visible=True)
        IMAGE_COLUMN = gr.Textbox(label='Image Column', value='image', visible=True)
        TRAIN_DATA_DIR = gr.Textbox(label='Train Data Dir', value='None', visible=True)
    with gr.Accordion(open=False, label="Image Processing") as IMAGE_PROCESSING_ACCORDION:
        CENTER_CROP = gr.Checkbox(label='Center Crop', value=False, visible=True)
        RANDOM_FLIP = gr.Checkbox(label='Random Flip', value=False, visible=True)
        RESOLUTION = gr.Slider(label='Resolution', value=1024, visible=True, step=64, minimum=256, maximum=4096)
    with gr.Accordion(open=False, label="Intervals") as INTERVALS_ACCORDION:
        CHECKPOINTING_STEPS = gr.Slider(label='Checkpointing Steps', value=500, visible=True, step=1, minimum=0, maximum=100000)
        MAX_TRAIN_SAMPLES = gr.Textbox(label='Max Train Samples', value='None', visible=True)
        MAX_TRAIN_STEPS = gr.Textbox(label='Max Train Steps', value='None', visible=False)
        NUM_TRAIN_EPOCHS = gr.Slider(label='Num Train Epochs', value=1, visible=True, step=1, minimum=0, maximum=100000)
        VALIDATION_EPOCHS = gr.Slider(label='Validation Epochs', value=1, visible=True, step=1, minimum=0, maximum=100)
    with gr.Accordion(open=False, label="Lora") as LORA_ACCORDION:
        RANK = gr.Slider(label='Rank', value=4, visible=True, step=1, minimum=0, maximum=100)
    with gr.Accordion(open=False, label="Learning Rate") as LEARNING_RATE_ACCORDION:
        LEARNING_RATE = gr.Slider(label='Learning Rate', value=5e-06, visible=True, step=0.01, minimum=0, maximum=1)
        LR_SCHEDULER = gr.Dropdown(label='Lr Scheduler', choices=['linear', 'cosine', 'cosine_with_restarts', 'polynomial', 'constant', 'constant_with_warmup'], value='constant', visible=True)
        LR_WARMUP_STEPS = gr.Slider(label='Lr Warmup Steps', value=500, visible=True, step=1, minimum=0, maximum=100000)
        SCALE_LR = gr.Checkbox(label='Scale Lr', value=False, visible=True)
    with gr.Accordion(open=False, label="Logging") as LOGGING_ACCORDION:
        LOGGING_DIR = gr.Textbox(label='Logging Dir', value='logs', visible=False)
        REPORT_TO = gr.Dropdown(label='Report To', choices=['all', 'tensorboard', 'wandb'], value='tensorboard', visible=True)
    with gr.Accordion(open=False, label="Optimizer") as OPTIMIZER_ACCORDION:
        ADAM_BETA1 = gr.Slider(label='Adam Beta1', value=0.9, visible=True, step=0.01, minimum=0, maximum=1)
        ADAM_BETA2 = gr.Slider(label='Adam Beta2', value=0.999, visible=True, step=0.01, minimum=0, maximum=1)
        ADAM_EPSILON = gr.Slider(label='Adam Epsilon', value=1e-08, visible=True, step=0.01, minimum=0, maximum=1)
        ADAM_WEIGHT_DECAY = gr.Slider(label='Adam Weight Decay', value=0.01, visible=True, step=0.01, minimum=0, maximum=1)
        MAX_GRAD_NORM = gr.Slider(label='Max Grad Norm', value=1.0, visible=True, step=0.1, minimum=0, maximum=1)
    with gr.Accordion(open=False, label="Performance") as PERFORMANCE_ACCORDION:
        ALLOW_TF32 = gr.Checkbox(label='Allow Tf32', value=True, visible=True)
        DATALOADER_NUM_WORKERS = gr.Slider(label='Dataloader Num Workers', value=1, visible=True, step=1, minimum=0, maximum=100)
        ENABLE_XFORMERS_MEMORY_EFFICIENT_ATTENTION = gr.Checkbox(label='Enable Xformers Memory Efficient Attention', value=True, visible=True)
        GRADIENT_CHECKPOINTING = gr.Checkbox(label='Gradient Checkpointing', value=True, visible=True)
        LOCAL_RANK = gr.Slider(label='Local Rank', value=-1, visible=True, step=1, minimum=0, maximum=100)
        MIXED_PRECISION = gr.Dropdown(label='Mixed Precision', choices=['no', 'fp16', 'bf16'], value='bf16', visible=True)
        NOISE_OFFSET = gr.Slider(label='Noise Offset', value=0, visible=True, step=0.01, minimum=0, maximum=1)
        PREDICTION_TYPE = gr.Dropdown(label='Prediction Type', choices=['epsilon', 'v_prediction'], value='None', visible=True)
        SEED = gr.Textbox(label='Seed', value='None', visible=True)
        SNR_GAMMA = gr.Textbox(label='Snr Gamma', value='None', visible=True)
        USE_8BIT_ADAM = gr.Checkbox(label='Use 8Bit Adam', value=True, visible=True)
    with gr.Accordion(open=False, label="Saving") as SAVING_ACCORDION:
        CHECKPOINTS_TOTAL_LIMIT = gr.Textbox(label='Checkpoints Total Limit', value='3', visible=True)
        HUB_MODEL_ID = gr.Textbox(label='Hub Model Id', value='None', visible=False)
        HUB_TOKEN = gr.Textbox(label='Hub Token', value='None', visible=False)
        PUSH_TO_HUB = gr.Checkbox(label='Push To Hub', value=False, visible=False)
    with gr.Accordion(open=False, label="Validation") as VALIDATION_ACCORDION:
        NUM_VALIDATION_IMAGES = gr.Slider(label='Num Validation Images', value=4, visible=True, step=1, minimum=0, maximum=100)
        VALIDATION_PROMPT = gr.Textbox(label='Validation Prompt', value='None', visible=True)
    manager.register_db_component("train_text_to_image_lora", GRADIENT_ACCUMULATION_STEPS, "gradient_accumulation_steps", True, "Number of updates steps to accumulate before performing a backward/update pass.")
    manager.register_db_component("train_text_to_image_lora", TRAIN_BATCH_SIZE, "train_batch_size", False, "Batch size (per device) for the training dataloader.")
    manager.register_db_component("train_text_to_image_lora", CAPTION_COLUMN, "caption_column", False, "The column of the dataset containing a caption or a list of captions.")
    manager.register_db_component("train_text_to_image_lora", DATASET_CONFIG_NAME, "dataset_config_name", True, "The config of the Dataset, leave as None if there\'s only one config.")
    manager.register_db_component("train_text_to_image_lora", DATASET_NAME, "dataset_name", False, "The name of the Dataset (from the HuggingFace hub) to train on (could be your own, possibly private, dataset). It can also be a path pointing to a local copy of a dataset in your filesystem, or to a folder containing files that 🤗 Datasets can understand.")
    manager.register_db_component("train_text_to_image_lora", IMAGE_COLUMN, "image_column", False, "The column of the dataset containing an image.")
    manager.register_db_component("train_text_to_image_lora", TRAIN_DATA_DIR, "train_data_dir", False, "A folder containing the training data. Folder contents must follow the structure described in https://huggingface.co/docs/datasets/image_dataset#imagefolder. In particular, a `metadata.jsonl` file must exist to provide the captions for the images. Ignored if `dataset_name` is specified.")
    manager.register_db_component("train_text_to_image_lora", CENTER_CROP, "center_crop", True, "Whether to center crop the input images to the resolution. If not set, the images will be randomly cropped. The images will be resized to the resolution first before cropping.")
    manager.register_db_component("train_text_to_image_lora", RANDOM_FLIP, "random_flip", True, "whether to randomly flip images horizontally")
    manager.register_db_component("train_text_to_image_lora", RESOLUTION, "resolution", False, "The resolution for input images, all the images in the train/validation dataset will be resized to this resolution")
    manager.register_db_component("train_text_to_image_lora", CHECKPOINTING_STEPS, "checkpointing_steps", False, "Save a checkpoint of the training state every X updates. These checkpoints are only suitable for resuming training using `--resume_from_checkpoint`.")
    manager.register_db_component("train_text_to_image_lora", MAX_TRAIN_SAMPLES, "max_train_samples", True, "For debugging purposes or quicker training, truncate the number of training examples to this value if set.")
    manager.register_db_component("train_text_to_image_lora", MAX_TRAIN_STEPS, "max_train_steps", False, "Total number of training steps to perform.  If provided, overrides num_train_epochs.")
    manager.register_db_component("train_text_to_image_lora", NUM_TRAIN_EPOCHS, "num_train_epochs", False, "")
    manager.register_db_component("train_text_to_image_lora", VALIDATION_EPOCHS, "validation_epochs", False, "Run fine-tuning validation every X epochs. The validation process consists of running the prompt `args.validation_prompt` multiple times: `args.num_validation_images`.")
    manager.register_db_component("train_text_to_image_lora", RANK, "rank", True, "The dimension of the LoRA update matrices.")
    manager.register_db_component("train_text_to_image_lora", LEARNING_RATE, "learning_rate", False, "Initial learning rate (after the potential warmup period) to use.")
    manager.register_db_component("train_text_to_image_lora", LR_SCHEDULER, "lr_scheduler", True, "The scheduler type to use. Choose between [\"linear\", \"cosine\", \"cosine_with_restarts\", \"polynomial\", \"constant\", \"constant_with_warmup\"]")
    manager.register_db_component("train_text_to_image_lora", LR_WARMUP_STEPS, "lr_warmup_steps", True, "Number of steps for the warmup in the lr scheduler.")
    manager.register_db_component("train_text_to_image_lora", SCALE_LR, "scale_lr", True, "Scale the learning rate by the number of GPUs, gradient accumulation steps, and batch size.")
    manager.register_db_component("train_text_to_image_lora", LOGGING_DIR, "logging_dir", False, "[TensorBoard](https://www.tensorflow.org/tensorboard) log directory. Will default to *output_dir/runs/**CURRENT_DATETIME_HOSTNAME***.")
    manager.register_db_component("train_text_to_image_lora", REPORT_TO, "report_to", False, "The integration to report the results and logs to. Supported platforms are `\"tensorboard\"` (default), `\"wandb\"` and `\"comet_ml\"`. Use `\"all\"` to report to all integrations.")
    manager.register_db_component("train_text_to_image_lora", ADAM_BETA1, "adam_beta1", True, "The beta1 parameter for the Adam optimizer.")
    manager.register_db_component("train_text_to_image_lora", ADAM_BETA2, "adam_beta2", True, "The beta2 parameter for the Adam optimizer.")
    manager.register_db_component("train_text_to_image_lora", ADAM_EPSILON, "adam_epsilon", True, "Epsilon value for the Adam optimizer")
    manager.register_db_component("train_text_to_image_lora", ADAM_WEIGHT_DECAY, "adam_weight_decay", True, "Weight decay to use.")
    manager.register_db_component("train_text_to_image_lora", MAX_GRAD_NORM, "max_grad_norm", True, "Max gradient norm.")
    manager.register_db_component("train_text_to_image_lora", ALLOW_TF32, "allow_tf32", True, "Whether or not to allow TF32 on Ampere GPUs. Can be used to speed up training. For more information, see https://pytorch.org/docs/stable/notes/cuda.html#tensorfloat-32-tf32-on-ampere-devices")
    manager.register_db_component("train_text_to_image_lora", DATALOADER_NUM_WORKERS, "dataloader_num_workers", True, "Number of subprocesses to use for data loading. 0 means that the data will be loaded in the main process.")
    manager.register_db_component("train_text_to_image_lora", ENABLE_XFORMERS_MEMORY_EFFICIENT_ATTENTION, "enable_xformers_memory_efficient_attention", False, "Whether or not to use xformers.")
    manager.register_db_component("train_text_to_image_lora", GRADIENT_CHECKPOINTING, "gradient_checkpointing", True, "Whether or not to use gradient checkpointing to save memory at the expense of slower backward pass.")
    manager.register_db_component("train_text_to_image_lora", LOCAL_RANK, "local_rank", True, "For distributed training: local_rank")
    manager.register_db_component("train_text_to_image_lora", MIXED_PRECISION, "mixed_precision", True, "Whether to use mixed precision. Choose between fp16 and bf16 (bfloat16). Bf16 requires PyTorch >= 1.10.and an Nvidia Ampere GPU.  Default to the value of accelerate config of the current system or the flag passed with the `accelerate.launch` command. Use this argument to override the accelerate config.")
    manager.register_db_component("train_text_to_image_lora", NOISE_OFFSET, "noise_offset", True, "The scale of noise offset.")
    manager.register_db_component("train_text_to_image_lora", PREDICTION_TYPE, "prediction_type", True, "The prediction_type that shall be used for training. Choose between \'epsilon\' or \'v_prediction\' or leave `None`. If left to `None` the default prediction type of the scheduler: `noise_scheduler.config.prediciton_type` is chosen.")
    manager.register_db_component("train_text_to_image_lora", SEED, "seed", True, "A seed for reproducible training.")
    manager.register_db_component("train_text_to_image_lora", SNR_GAMMA, "snr_gamma", True, "SNR weighting gamma to be used if rebalancing the loss. Recommended value is 5.0. More details here: https://arxiv.org/abs/2303.09556.")
    manager.register_db_component("train_text_to_image_lora", USE_8BIT_ADAM, "use_8bit_adam", True, "Whether or not to use 8-bit Adam from bitsandbytes.")
    manager.register_db_component("train_text_to_image_lora", CHECKPOINTS_TOTAL_LIMIT, "checkpoints_total_limit", True, "Max number of checkpoints to store.")
    manager.register_db_component("train_text_to_image_lora", HUB_MODEL_ID, "hub_model_id", False, "The name of the repository to keep in sync with the local `output_dir`.")
    manager.register_db_component("train_text_to_image_lora", HUB_TOKEN, "hub_token", False, "The token to use to push to the Model Hub.")
    manager.register_db_component("train_text_to_image_lora", PUSH_TO_HUB, "push_to_hub", False, "Whether or not to push the model to the Hub.")
    manager.register_db_component("train_text_to_image_lora", NUM_VALIDATION_IMAGES, "num_validation_images", True, "Number of images that should be generated during validation with `validation_prompt`.")
    manager.register_db_component("train_text_to_image_lora", VALIDATION_PROMPT, "validation_prompt", True, "A prompt that is sampled during training for inference.")