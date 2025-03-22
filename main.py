import streamlit as st
import fitz  # PyMuPDF
from io import BytesIO


# Hàm chuyển đổi từng trang PDF thành hình ảnh
def pdf_to_images(pdf_file):
    # Mở file PDF
    doc = fitz.open(pdf_file)

    # Danh sách để chứa các hình ảnh của các trang PDF
    images = []

    # Duyệt qua từng trang và chuyển đổi thành hình ảnh
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)  # Tải trang
        pix = page.get_pixmap()  # Chuyển đổi trang thành hình ảnh
        img_bytes = pix.tobytes()  # Chuyển hình ảnh thành bytes
        images.append(img_bytes)

    return images


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
    <div class="container">
        <div class="img-container">
            <img src="https://appetiser.com.au/wp-content/uploads/2019/03/Google-V8.png.webp" width="700" style="channels='RGB'">
        </div>
        <h1>V8 Engine</h1>
        <p>Đây là nội dung của bạn.</p>
        <!-- Thêm nội dung của bạn sau đây -->
    </div>
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
        <p>1. Giới thiệu tổng quát V8 Engine</p>
        <p>2. Fast Property Access</p>
        <p>3. Garbage Collection</p>
        <p>4. Pipeline</p>
        <p>5. Tổng kết</p>
    </div>
    """, unsafe_allow_html=True)

# Tab
tab1, tab2 = st.tabs(["Bài Đăng", "Demo"])

with tab1:
    st.markdown("<h2 style='color: #FFC81B;'>F-Code [Techaway 2024]</h2>", unsafe_allow_html=True)
    st.markdown("#### **F-Code authors:**")
    st.write("""
        - *Phạm Hoàng Tuấn - SE200947*
        - *Võ Đức Trí - SE204214*
    """)

st.markdown("""
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-0.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-1.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-2.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-3.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-4.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-5.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-6.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-7.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-8.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-9.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-10.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-11.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-12.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-13.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-14.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-15.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-16.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-17.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-18.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-19.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-20.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-21.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-22.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-23.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-24.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-25.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-26.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-27.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-28.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-29.png)
![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/content-images-30.png)



""")
