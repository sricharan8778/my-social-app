
import streamlit as st

st.set_page_config(page_title="My Social App", page_icon="📱")

st.title("📱 My Social App")
st.write("Share your world through photos!")

if "posts" not in st.session_state:
    st.session_state.posts = []

st.header("Create a post")

with st.form("post_form", clear_on_submit=True):
    username = st.text_input("Your username")
    caption = st.text_area("Write a caption")
    photo = st.file_uploader(
        "Choose a photo",
        type=["jpg", "jpeg", "png", "webp"]
    )
    submitted = st.form_submit_button("Publish Post")

if submitted:
    if not username.strip():
        st.warning("Please enter your username.")
    elif photo is None:
        st.warning("Please choose a photo.")
    else:
        st.session_state.posts.insert(
            0,
            {
                "username": username.strip(),
                "caption": caption.strip(),
                "photo": photo.getvalue(),
            },
        )
        st.success("Your photo post was published!")

st.divider()
st.header("Home Feed")

if not st.session_state.posts:
    st.info("No posts yet. Upload the first photo!")

for post in st.session_state.posts:
    st.subheader("👤 " + post["username"])
    if post["caption"]:
        st.write(post["caption"])
    st.image(post["photo"], use_container_width=True)
    st.divider()

