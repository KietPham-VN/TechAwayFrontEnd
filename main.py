import streamlit as st

# Thiết lập cấu hình trang Streamlit
st.set_page_config(
    page_title="Frontend Thế Hệ Mới - Hành Trình Bứt Phá cùng cursor ai & Claude 3.7 sonnet & react 19🚀🚀.",
    page_icon="./assets/icons/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Nội dung chính của trang
st.write(
    """
    <style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .img-container {
        margin-bottom: 20px;
    }
      h1 {
        font-size: 80px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.header("Nội dung bài viết")
    source_vid = st.sidebar.write("""
    <style>
        .toc {
            background-color: #0E1117;
            border-radius: 10px;
        }
        .toc p {
            font-size: 15px;
            margin: 0;
            padding: 10px;
            cursor: pointer;
            z-index: 2;
        }
    </style>
    <div class="toc">
        <p>1. Lời mở đầu</p>
        <p>2. Tăng tốc lập trình với IDE hiệu quả</p>
        <p>3. Top 4 công cụ AI mạnh mẽ hỗ trợ lập trình</p>
        <p>4. Các Extension hữu ích cho VSCode đối với dân FrontEnd</p>
        <p>5. React 19 - Sự thay đổi mạnh mẽ</p>
        <p>6. Thư viện hỗ trợ dự án React trở nên xịn sò hơn</p>
        <p>7. Cách làm 1 project FrontEnd hiệu quả</p>
        <p>8. Tổng kết</p>
                                  
    </div>
    """, unsafe_allow_html=True)

# Tab
tab1, tab2 = st.tabs(["Bài Đăng", "Demo"])

with tab1:
    st.markdown("<h2 style='color: #FFC81B;'>F-Code [Techaway 2025]</h2>", unsafe_allow_html=True)
    st.markdown("#### **F-Code authors:**")
    st.write("""
        - *Phạm Hoàng Tuấn - SE200947*
        - *Võ Đức Trí - SE204214*
    """)

st.markdown("""
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-0.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-1.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-2.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-3.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-4.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-5.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-6.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-7.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-8.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-9.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-10.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-11.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-12.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-13.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-14.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-15.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-16.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-17.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-18.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-19.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-20.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-21.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-22.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-23.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-24.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-25.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-26.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-27.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-28.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-29.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-30.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-31.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-32.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-33.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-34.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-35.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-36.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-37.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-38.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-39.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-40.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-41.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-42.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-43.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-44.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-45.jpg)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayFrontEnd/main/assets/images/content-images-46.jpg)
""", unsafe_allow_html=True)

