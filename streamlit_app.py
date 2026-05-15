import streamlit as st

# 페이지 제목
st.title("자기소개 페이지")

# 인사말
st.header("안녕하세요!")
st.write("저는 허이레입니다. 청주교대 대학생이야. 이 페이지를 통해 저에 대해 더 알아보세요!")

# 프로필 이미지 (선택적 - 나중에 이미지 파일 경로를 추가하세요)
# st.image("profile.jpg", width=200)

# 간단한 소개
st.subheader("소개")
st.write("""
청주교대 26학번 체육교육과 예비교사야. 
운동을 좋아해. 특히 테니스를 좋아하고, 먹는것도 좋아해서 삼겹살을 아주 좋아하고 용인에 살아!!
""")

# 연락처 정보
st.subheader("연락처")
st.write("이메일: donaid22@naver.com")
st.write("GitHub: [https://github.com/yourusername]")
st.write("LinkedIn: [https://linkedin.com/in/yourprofile]")

# 관심사 또는 기술 스킬
st.subheader("관심사")
st.write("- 테니스")
st.write("- 음악")
st.write("- 음식")

# 추가 섹션 (예: 경력, 프로젝트 등)
st.subheader("경력")
st.write("현재: 청주교대 대학생")
st.write("이전: 학생")

st.subheader("프로젝트")
st.write("- 자기소개")
st.write("- 취미")

# 푸터
st.write("---")
st.write("이 페이지는 Streamlit으로 만들어졌습니다.")
