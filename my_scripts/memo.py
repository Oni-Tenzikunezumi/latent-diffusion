# CUDA_VISIBLE_DEVICES =<GPU_ID> python main.py --base configs/autoencoder/<config_spec>.yaml -t --gpus 0,
# CUDA_VISIBLE_DEVICES =0 python main.py --base configs/autoencoder/celebahq-ldm-vq-4.yaml -t --gpus 0,

"""
    get_num_classes
        => torchmetricsのバージョンが新しすぎる
        https://lightning.ai/docs/torchmetrics/stable/generated/CHANGELOG.html#id85
        https://lightning.ai/docs/torchmetrics/stable/pages/quickstart.html
        pip install torchmetrics==0.7.3

    packaging.version.InvalidVersion: Invalid version: '0.10.1,<0.11'
        => パッケージのエラー
        https://github.com/CompVis/latent-diffusion/issues/207
        pip install kornia==0.5.0
        pip install transformers==4.10.2

    Torch not compiled with CUDA enabled
        => cudaのモジュールが対応してない（多分）
        https://qiita.com/sakusaku3939/items/1a133729c7f38e8403ce
        https://pytorch.org/get-started/previous-versions/
        # CUDA 11.0
        pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

    OSError: [Errno 22] Invalid argument
        => 普通にパスに入れちゃいけない文字
        "prompt" -> 'prompt'

    conda create -n 新しい環境名 --clone 複製したいベースの環境名
"""


"""
    where <config_spec> is one of {
        celebahq-ldm-vq-4(f=4, VQ-reg. autoencoder, spatial size 64x64x3),
        ffhq-ldm-vq-4(f=4, VQ-reg. autoencoder, spatial size 64x64x3),
        lsun_bedrooms-ldm-vq-4(f=4, VQ-reg. autoencoder, spatial size 64x64x3),
        lsun_churches-ldm-vq-4(f=8, KL-reg. autoencoder, spatial size 32x32x4),
        cin-ldm-vq-8(f=8, VQ-reg. autoencoder, spatial size 32x32x4)}.
"""

aaaa = 1
print(aaaa)