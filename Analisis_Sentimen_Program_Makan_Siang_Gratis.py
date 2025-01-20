import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import emoji

file_path = '/content/Dataset_Program_Makan_Siang_Gratis - Sheet1.csv'

def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    dataset[['Tweet', 'Sentiment']] = dataset['Tweet,Sentiment'].str.split(',', 1, expand=True)
    return dataset.drop(columns=['Tweet,Sentiment'])

def remove_emoji(text):
    return emoji.replace_emoji(text, replace='')

def sentiment_distribution(dataset):
    sentiment_counts = dataset['Sentiment'].value_counts()
    plt.figure(figsize=(8, 6))
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'], alpha=0.7, edgecolor='black')
    plt.title('Distribusi Sentimen', fontsize=16)
    plt.xlabel('Sentimen', fontsize=12)
    plt.ylabel('Jumlah', fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    return sentiment_counts.to_dict()

def extract_examples(dataset):
    examples = {}
    for sentiment in ['Positive', 'Neutral', 'Negative']:
        examples[sentiment] = dataset[dataset['Sentiment'] == sentiment]['Tweet'].head(1).tolist()
    return examples

def generate_wordcloud(dataset):
    sentiments = dataset['Sentiment'].unique()
    for sentiment in sentiments:
        text = " ".join(dataset[dataset['Sentiment'] == sentiment]['Tweet'].apply(remove_emoji).astype(str))

        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title(f'WordCloud for {sentiment}', fontsize=16)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

def train_model(dataset):
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(dataset['Tweet'].apply(remove_emoji))
    y = dataset['Sentiment']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    confusion = confusion_matrix(y_test, y_pred)

    print("Laporan Klasifikasi:")
    print(report)

    return model, vectorizer, confusion

def plot_confusion_matrix(confusion):
    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Positive', 'Neutral', 'Negative'],
                yticklabels=['Positive', 'Neutral', 'Negative'])
    plt.title('Confusion Matrix', fontsize=16)
    plt.xlabel('Predicted', fontsize=12)
    plt.ylabel('Actual', fontsize=12)
    plt.tight_layout()
    plt.show()

def step_1_statistics(dataset):
    sentiment_stats = sentiment_distribution(dataset)
    print("Distribusi Sentimen:", sentiment_stats)

def step_2_examples(dataset):
    examples = extract_examples(dataset)
    print("Contoh Kalimat per Sentimen:", examples)

def step_3_analysis(dataset):
    model, vectorizer, confusion = train_model(dataset)
    plot_confusion_matrix(confusion)

def step_4_visualization(dataset):
    generate_wordcloud(dataset)

def main():
    dataset = pd.read_csv(file_path)
    dataset[['Tweet', 'Sentiment']] = dataset['Tweet,Sentiment'].str.split(',', n=1, expand=True)

    print("=== Step 1: Statistik Sentimen ===")
    step_1_statistics(dataset)

    print("\n=== Step 2: Contoh Kalimat per Sentimen ===")
    step_2_examples(dataset)

    print("\n=== Step 3: Analisis Model ===")
    step_3_analysis(dataset)

    print("\n=== Step 4: Visualisasi Insights ===")
    step_4_visualization(dataset)

    print("\nAnalisis selesai. Semua hasil telah ditampilkan.")

if __name__ == "__main__":
    main()