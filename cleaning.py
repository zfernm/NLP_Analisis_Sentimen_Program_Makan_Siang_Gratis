import pandas as pd

file_names = [
    "program_makan_siang_gratis_1.csv",
    "program_makan_siang_gratis_2.csv",
    "program_makan_siang_gratis_3.csv",
    "program_makan_siang_gratis_4.csv",
    "program_makan_siang_gratis_5.csv",
    "program_makan_siang_gratis_6.csv",
    "program_makan_siang_gratis_7.csv",
    "program_makan_siang_gratis_8.csv",
    "program_makan_siang_gratis_9.csv",
    "program_makan_siang_gratis_10.csv",
    "program_makan_siang_gratis_11.csv",
    "program_makan_siang_gratis_12.csv"
]

def clean_and_merge_datasets(file_names):
    combined_df = pd.DataFrame()  

    for file in file_names:
        df = pd.read_csv(file)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    cleaned_df = combined_df.drop_duplicates(subset=["Tweet"])

    return cleaned_df

cleaned_data = clean_and_merge_datasets(file_names)

cleaned_data.to_csv("Analisis_Sentimen_Program_Makan_Siang_Gratis.csv", index=False)

print("Data telah dibersihkan dan disimpan ke 'Analisis_Sentimen_Program_Makan_Siang_Gratis.csv'.")