# Feature

- This tool will generate batch QR image for detail from codeList.txt
- Exported QR folder will be in "output/"

# Step to use

- Fill content in codeList.txt
- Run generate_qr_from_csv.py

# codeList.txt structure

- Example: 4024685-8,W8OPCAY04DGZ,B,MSA_20231122
    - 4024685-8: part number
    - W8OPCAY04DGZ: SKU
    - B: part condition
    - MSA_20231122: note for generated file name

# File name structure

- {note}_{partNumber}_{SKU}.png
