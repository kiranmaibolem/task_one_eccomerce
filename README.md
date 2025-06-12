# 🛒 Ecommerce Sales Data Cleaning Project

This project performs automated ETL (Extract, Transform, Load) on multiple raw ecommerce `.csv` files and outputs a clean, combined dataset.

## 📁 Project Structure

```
project-root/
├── cleaned_ecommerce_data.csv         # Final cleaned dataset
├── app.py                              # Python script for preprocessing
├── ecommerce_dataset/                 # (Optional) Folder with raw CSVs
│   ├── file1.csv
│   ├── file2.csv
│   └── ...
├── README.md                          # This file
```

## 🚀 Features

* Combines multiple `.csv` files into one DataFrame
* Cleans and standardizes column names
* Converts `date` columns to datetime format
* Handles missing values based on column type
* Encodes categorical columns like `status`, `fulfilment`, `sales_channel`
* Scales numeric columns like `qty`, `amount`
* Exports the cleaned dataset as `cleaned_ecommerce_data.csv`

## 🧪 Technologies Used

* Python 3
* Pandas
* Scikit-learn (for encoding and scaling)

## ⚙️ How to Run

1. Place all your raw `.csv` files inside the `ecommerce_dataset` folder.
2. Update the `folder_path` in `rd.py` to point to that folder.
3. Run the script:

```bash
python rd.py
```

4. The cleaned file will be saved as `cleaned_ecommerce_data.csv`

## 📌 Notes

* Make sure all `.csv` files have similar structures for smooth merging.
* If column `date` is missing or malformed, it will be handled safely.

---

✅ Maintained by: `Kiranmai Bolem`

Feel free to fork or contribute!
