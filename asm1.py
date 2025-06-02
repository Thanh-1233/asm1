import streamlit as st

st.title("Ứng dụng đếm từ và đọc file tần suất")

chuc_nang = st.radio("Chọn chức năng:", ["Đếm từ trong file văn bản", "Hiển thị từ điển tần suất từ file txt"])

if chuc_nang == "Đếm từ trong file văn bản":
    tai_file = st.file_uploader("Tải lên file văn bản (.txt)", type=["txt"])
    
    if tai_file is not None:
        text = tai_file.read().decode("utf-8").lower()
        
        raw_words = text.replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ").replace("\n", " ")
        words = raw_words.split()

        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        with open("frequency.txt", "w", encoding="utf-8") as f:
            for word, count in word_freq.items():
                f.write(f"{word}: {count}\n")

        st.success("Đã phân tích và lưu kết quả vào 'frequency.txt'")
        st.write(word_freq)

elif chuc_nang == "Hiển thị từ điển tần suất từ file txt":
    file_da_tai = st.file_uploader("Tải lên file tần suất (.txt)", type=["txt"])
    
    if file_da_tai is not None:
        tan_suat = {}
        lines = file_da_tai.read().decode("utf-8").splitlines()
        for line in lines:
            if ":" in line:
                word, count = line.split(":", 1)
                tan_suat[word.strip()] = int(count.strip())
        
        st.write("Từ điển tần suất đã nạp:")
        st.write(tan_suat)
