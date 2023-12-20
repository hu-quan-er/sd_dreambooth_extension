let more_hints = {
    "Gradient Accumulation Steps": "Number of updates steps to accumulate before performing a backward/update pass.",
    "Train Batch Size": "Batch size (per device) for the training dataloader.",
    "Caption Column": "The column of the dataset containing a caption or a list of captions.",
    "Conditioning Image Column": "The column of the dataset containing the adapter conditioning image.",
    "Dataset Config Name": "The config of the Dataset, leave as None if there's only one config.",
    "Dataset Name": "The name of the Dataset (from the HuggingFace hub) to train on (could be your own, possibly private, dataset). It can also be a path pointing to a local copy of a dataset in your filesystem, or to a folder containing files that \ud83e\udd17 Datasets can understand.",
    "Image Column": "The column of the dataset containing an image.",
    "Proportion Empty Prompts": "Proportion of image prompts to be replaced with empty strings. Defaults to 0 (no prompt replacement).",
    "Train Data Dir": "A folder containing the training data. Folder contents must follow the structure described in https://huggingface.co/docs/datasets/image_dataset#imagefolder. In particular, a `metadata.jsonl` file must exist to provide the captions for the images. Ignored if `dataset_name` is specified.",
    "Resolution": "The resolution for input images, all the images in the train/validation dataset will be resized to this resolution",
    "Checkpointing Steps": "Save a checkpoint of the training state every X updates. These checkpoints can be used both as final checkpoints in case they are better than the last checkpoint, and are also suitable for resuming training using `--resume_from_checkpoint`.",
    "Max Train Samples": "For debugging purposes or quicker training, truncate the number of training examples to this value if set.",
    "Max Train Steps": "Total number of training steps to perform.  If provided, overrides num_train_epochs.",
    "Num Train Epochs": "",
    "Validation Steps": "Run validation every X steps. Validation consists of running the prompt `args.validation_prompt` multiple times: `args.num_validation_images` and logging the images.",
    "Learning Rate": "Initial learning rate (after the potential warmup period) to use.",
    "Lr Num Cycles": "Number of hard resets of the lr in cosine_with_restarts scheduler.",
    "Lr Power": "Power factor of the polynomial scheduler.",
    "Lr Scheduler": "The scheduler type to use. Choose between [\"linear\", \"cosine\", \"cosine_with_restarts\", \"polynomial\", \"constant\", \"constant_with_warmup\"]",
    "Lr Warmup Steps": "Number of steps for the warmup in the lr scheduler.",
    "Scale Lr": "Scale the learning rate by the number of GPUs, gradient accumulation steps, and batch size.",
    "Logging Dir": "[TensorBoard](https://www.tensorflow.org/tensorboard) log directory. Will default to *output_dir/runs/**CURRENT_DATETIME_HOSTNAME***.",
    "Report To": "The integration to report the results and logs to. Supported platforms are `\"tensorboard\"` (default), `\"wandb\"` and `\"comet_ml\"`. Use `\"all\"` to report to all integrations.",
    "Tracker Project Name": "The `project_name` argument passed to Accelerator.init_trackers for more information see https://huggingface.co/docs/accelerate/v0.17.0/en/package_reference/accelerator#accelerate.Accelerator",
    "Controlnet Model Name Or Path": "Path to pretrained controlnet model or model identifier from huggingface.co/models. If not specified controlnet weights are initialized from unet.",
    "Adam Beta1": "The beta1 parameter for the Adam optimizer.",
    "Adam Beta2": "The beta2 parameter for the Adam optimizer.",
    "Adam Epsilon": "Epsilon value for the Adam optimizer",
    "Adam Weight Decay": "Weight decay to use.",
    "Max Grad Norm": "Max gradient norm.",
    "Allow Tf32": "Whether or not to allow TF32 on Ampere GPUs. Can be used to speed up training. For more information, see https://pytorch.org/docs/stable/notes/cuda.html#tensorfloat-32-tf32-on-ampere-devices",
    "Dataloader Num Workers": "Number of subprocesses to use for data loading. 0 means that the data will be loaded in the main process.",
    "Enable Xformers Memory Efficient Attention": "Whether or not to use xformers.",
    "Gradient Checkpointing": "Whether or not to use gradient checkpointing to save memory at the expense of slower backward pass.",
    "Mixed Precision": "Whether to use mixed precision. Choose between fp16 and bf16 (bfloat16). Bf16 requires PyTorch >= 1.10.and an Nvidia Ampere GPU.  Default to the value of accelerate config of the current system or the flag passed with the `accelerate.launch` command. Use this argument to override the accelerate config.",
    "Seed": "A seed for reproducible training.",
    "Set Grads To None": "Save more memory by using setting grads to None instead of zero. Be aware, that this changes certain behaviors, so disable this argument if it causes any problems. More info: https://pytorch.org/docs/stable/generated/torch.optim.Optimizer.zero_grad.html",
    "Use 8Bit Adam": "Whether or not to use 8-bit Adam from bitsandbytes.",
    "Checkpoints Total Limit": "Max number of checkpoints to store.",
    "Hub Model Id": "The name of the repository to keep in sync with the local `output_dir`.",
    "Hub Token": "The token to use to push to the Model Hub.",
    "Push To Hub": "Whether or not to push the model to the Hub.",
    "Num Validation Images": "Number of images that should be generated during validation with `validation_prompt`.",
    "Validation Image": "A set of paths to the t2iadapter conditioning image be evaluated every `--validation_steps` and logged to `--report_to`. Provide either a matching number of `--validation_prompt`s, a a single `--validation_prompt` to be used with all `--validation_image`s, or a single `--validation_image` that will be used with all `--validation_prompt`s.",
    "Validation Prompt": "A prompt that is used during validation to verify that the model is learning.",
    "Crops Coords Top Left H": "Coordinate for (the height) to be included in the crop coordinate embeddings needed by SDXL UNet.",
    "Crops Coords Top Left W": "Coordinate for (the height) to be included in the crop coordinate embeddings needed by SDXL UNet.",
    "Pretrained Vae Model Name Or Path": "Path to pretrained VAE model with better numerical stability. More details: https://github.com/huggingface/diffusers/pull/4038.",
    "Sample Batch Size": "Batch size (per device) for sampling images.",
    "Class Data Dir": "A folder containing the training data of class images.",
    "Class Labels Conditioning": "The optional `class_label` conditioning to pass to the unet, available values are `timesteps`.",
    "Class Prompt": "The prompt to specify images in the same class as provided instance images.",
    "Instance Data Dir": "A folder containing the training data. ",
    "Instance Prompt": "The prompt with identifier specifying the instance, e.g. 'photo of a TOK dog', 'in the style of TOK'",
    "Num Class Images": "Minimal class images for prior preservation loss. If there are not enough images already present in class_data_dir, additional images will be sampled with class_prompt.",
    "Prior Loss Weight": "The weight of prior preservation loss.",
    "With Prior Preservation": "Flag to add prior preservation loss.",
    "Center Crop": "Whether to center crop the input images to the resolution. If not set, the images will be randomly cropped. The images will be resized to the resolution first before cropping.",
    "Local Rank": "For distributed training: local_rank",
    "Offset Noise": "Fine-tuning against a modified noise See: https://www.crosslabs.org//blog/diffusion-with-offset-noise for more information.",
    "Pre Compute Text Embeddings": "Whether or not to pre-compute text embeddings. If text embeddings are pre-computed, the text encoder will not be kept in memory during training and will leave more GPU memory available for training the rest of the model. This is not compatible with `--train_text_encoder`.",
    "Prior Generation Precision": "Choose prior generation precision between fp32, fp16 and bf16 (bfloat16). Bf16 requires PyTorch >= 1.10.and an Nvidia Ampere GPU.  Default to  fp16 if a GPU is available else fp32.",
    "Snr Gamma": "SNR weighting gamma to be used if rebalancing the loss. Recommended value is 5.0. More details here: https://arxiv.org/abs/2303.09556.",
    "Text Encoder Use Attention Mask": "Whether to use attention mask for the text encoder",
    "Tokenizer Max Length": "The maximum length of the tokenizer. If not set, will default to the tokenizer's max length.",
    "Train Text Encoder": "Whether to train the text encoder. If set, the text encoder should be float32 precision.",
    "Skip Save Text Encoder": "Set to not save text encoder",
    "Validation Images": "Optional set of images to use for validation. Used when the target pipeline takes an initial image as input such as when training image variation or superresolution.",
    "Validation Scheduler": "Select which scheduler to use for validation. DDPMScheduler is recommended for DeepFloyd IF.",
    "Validation Epochs": "Run fine-tuning validation every X epochs. The validation process consists of running the prompt `args.validation_prompt` multiple times: `args.num_validation_images`.",
    "Rank": "The dimension of the LoRA update matrices.",
    "Repeats": "How many times to repeat the training data.",
    "Text Encoder Lr": "Text encoder learning rate to use.",
    "Adam Weight Decay Text Encoder": "Weight decay to use for text_encoder",
    "Optimizer": "The optimizer type to use. Choose between [\"AdamW\", \"prodigy\"]",
    "Prodigy Beta3": "coefficients for computing the Prodidy stepsize using running averages. If set to None, uses the value of square root of beta2. Ignored if optimizer is adamW",
    "Prodigy Decouple": "Use AdamW style decoupled weight decay",
    "Prodigy Safeguard Warmup": "Remove lr from the denominator of D estimate to avoid issues during warm-up stage. True by default. Ignored if optimizer is adamW",
    "Prodigy Use Bias Correction": "Turn on Adam's bias correction. True by default. Ignored if optimizer is adamW",
    "Detection Resolution": "The resolution for input images, all the images in the train/validation dataset will be resized to this resolution",
    "Adapter Model Name Or Path": "Path to pretrained adapter model or model identifier from huggingface.co/models. If not specified adapter weights are initialized w.r.t the configurations of SDXL.",
    "Input Perturbation": "The scale of input perturbation. Recommended 0.1.",
    "Random Flip": "whether to randomly flip images horizontally",
    "Noise Offset": "The scale of noise offset.",
    "Prediction Type": "The prediction_type that shall be used for training. Choose between 'epsilon' or 'v_prediction' or leave `None`. If left to `None` the default prediction type of the scheduler: `noise_scheduler.config.prediciton_type` is chosen.",
    "Use Ema": "Whether to use EMA model.",
    "Validation Prompts": "A set of prompts evaluated every `--validation_epochs` and logged to `--report_to`.",
    "Timestep Bias Begin": "When using `--timestep_bias_strategy=range`, the beginning (inclusive) timestep to bias. Defaults to zero, which equates to having no specific bias.",
    "Timestep Bias End": "When using `--timestep_bias_strategy=range`, the final timestep (inclusive) to bias. Defaults to 1000, which is the number of timesteps that Stable Diffusion is trained on.",
    "Timestep Bias Multiplier": "The multiplier for the bias. Defaults to 1.0, which means no bias is applied. A value of 2.0 will double the weight of the bias, and a value of 0.5 will halve it.",
    "Timestep Bias Portion": "The portion of timesteps to bias. Defaults to 0.25, which 25% of timesteps will be biased. A value of 0.5 will bias one half of the timesteps. The value provided for `--timestep_bias_strategy` determines whether the biased portions are in the earlier or later timesteps.",
    "Timestep Bias Strategy": "The timestep bias strategy, which may help direct the model toward learning low or high frequency details. Choices: ['earlier', 'later', 'range', 'none']. The default is 'none', which means no bias is applied, and training proceeds normally. The value of 'later' will increase the frequency of the model's final training timesteps."
}