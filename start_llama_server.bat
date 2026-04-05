@echo off
:: Configure model paths - update these if your models are in a different location
set MODEL_PATH=%USERPROFILE%\.cache\huggingface\hub\models--unsloth--gemma-4-e4b-it-gguf\snapshots\315e03409eb1cdde302488d66e586dea1e82aad1\gemma-4-E4B-it-UD-Q4_K_XL.gguf
set MMPROJ_PATH=%USERPROFILE%\.cache\huggingface\hub\models--unsloth--gemma-4-e4b-it-gguf\snapshots\315e03409eb1cdde302488d66e586dea1e82aad1\mmproj-BF16.gguf

:: Check if model files exist
if not exist %MODEL_PATH% (
    echo ERROR: Model file not found: %MODEL_PATH%
    echo Please download the Gemma 4 E4B GGUF model from HuggingFace
    echo https://huggingface.co/unsloth/gemma-4-e4b-it-gguf
    pause
    exit /b 1
)

if not exist %MMPROJ_PATH% (
    echo ERROR: Multimodal projector not found: %MMPROJ_PATH%
    echo Please ensure the mmproj file is in the HuggingFace cache
    pause
    exit /b 1
)

echo Starting Gemma 4 E4B Server with Multimodal Support...
echo Model: %MODEL_PATH%
echo Projector: %MMPROJ_PATH%

llama-server -m %MODEL_PATH% --mmproj %MMPROJ_PATH% --ctx-size 131072 --port 8080
pause
