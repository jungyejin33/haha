import streamlit as st

product_db = {
    "P001": {"name": "นมเปรี้ยว", "price": 20, "exp": "10-06-2026", "info": "โปรตีน 5g"},
}

# ดึงรหัสสินค้า
product_id = st.query_params.get("id", "P001")
item = product_db.get(product_id)

st.title(f"สินค้า: {item['name']}")

# ระบบสลับสถานะ
if "mode" not in st.session_state:
    st.session_state.mode = "customer"

# เมนูเปลี่ยนโหมด (ซ่อนไว้หรือวางไว้ล่างสุด)
mode_select = st.sidebar.radio("สถานะการใช้งาน:", ["ลูกค้า", "พนักงาน"])
if mode_select == "พนักงาน" and "auth" not in st.session_state:
    pwd = st.sidebar.text_input("รหัสพนักงาน:", type="password")
    if st.sidebar.button("ยืนยัน"):
        if pwd == "1234":
            st.session_state.auth = True
            st.session_state.mode = "staff"
            st.rerun()
else:
    st.session_state.mode = "customer"

# แสดงผลตามสถานะ
if st.session_state.mode == "staff" and st.session_state.get("auth"):
    st.success("โหมดพนักงาน: จัดการสต๊อก / คำนวณราคา")
    st.write(f"ราคา: {item['price']} บาท | วันหมดอายุ: {item['exp']}")
else:
    st.write(f"ราคา: {item['price']} บาท")
    st.write(f"รายละเอียด: {item['info']}")
