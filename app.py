import streamlit as st

# ฐานข้อมูลสินค้า
product_db = {
    "P001": {
        "name": "นมเปรี้ยว", "price": 20, "exp": "10-06-2026", "mfg": "01-06-2026",
        "stock": 150, "allergy": "นมวัว", "instruction": "เก็บในอุณหภูมิเย็น", "nutrition": "โปรตีน 5g"
    }
}

st.title("ระบบจัดการสินค้า 🛒")

# 1. ระบบจัดการสถานะพนักงาน
if "auth" not in st.session_state:
    st.session_state.auth = False

# เมนูพนักงานใน Sidebar
with st.sidebar:
    st.header("สำหรับพนักงาน")
    if not st.session_state.auth:
        pwd = st.text_input("รหัสผ่านพนักงาน:", type="password")
        if st.button("เข้าสู่โหมดพนักงาน"):
            if pwd == "1234":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("รหัสผิด!")
    else:
        st.success("คุณล็อกอินแล้ว")
        if st.button("ออกจากระบบ"):
            st.session_state.auth = False
            st.rerun()

# 2. การแสดงผล
product_id = st.query_params.get("id", "P001")
item = product_db.get(product_id)

if item:
    st.subheader(f"สินค้า: {item['name']}")
    
    # ถ้าพนักงานล็อกอินอยู่ ให้โชว์ข้อมูลลึก
    if st.session_state.auth:
        st.write("---")
        st.warning("⚠️ โหมดพนักงาน: ข้อมูลภายใน")
        col1, col2 = st.columns(2)
        col1.metric("สต๊อกคงเหลือ", f"{item['stock']} ชิ้น")
        col2.metric("ราคาขาย", f"{item['price']} บาท")
        st.write(f"**วันผลิต:** {item['mfg']} | **หมดอายุ:** {item['exp']}")
        st.write(f"**รายละเอียดเพิ่มเติม:** {item['instruction']}")
    else:
        # ลูกค้าเห็นแค่ข้อมูลจำเป็น
        st.write(f"ราคา: {item['price']} บาท")
        st.write(f"ข้อมูลแพ้อาหาร: {item['allergy']}")
        st.write(f"โภชนาการ: {item['nutrition']}")
else:
    st.error("ไม่พบสินค้า")

