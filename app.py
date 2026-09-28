import streamlit as st
from datetime import datetime
import random

# ============ PAGE CONFIG ============
st.set_page_config(
    page_title="Hotel POS System",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============ CUSTOM CSS (Graphics Design) ============
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #ff6b6b 0%, #ffa500 50%, #ffcc00 100%);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        color: white;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        margin-bottom: 25px;
    }
    .main-header h1 {
        font-size: 45px;
        margin: 0;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
        font-family: 'Arial Black', sans-serif;
    }
    .main-header p {
        font-size: 18px;
        margin-top: 8px;
        font-style: italic;
    }
    .food-card {
        background: white;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s;
        border: 2px solid #ffcc00;
        margin-bottom: 10px;
    }
    .food-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(255,107,107,0.4);
    }
    .price-tag {
        background: linear-gradient(135deg, #28a745, #20c997);
        color: white;
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        font-size: 16px;
    }
    .category-title {
        color: #ff6b6b;
        font-size: 28px;
        font-weight: bold;
        border-bottom: 3px solid #ffcc00;
        padding-bottom: 8px;
        margin: 25px 0 15px 0;
    }
    .bill-box {
        background: linear-gradient(135deg, #fff9e6, #ffe6cc);
        padding: 20px;
        border-radius: 15px;
        border: 3px dashed #ff6b6b;
        font-family: 'Courier New', monospace;
    }
    .receipt {
        background: #ffffff;
        padding: 25px;
        border-radius: 10px;
        border: 2px solid #333;
        font-family: 'Courier New', monospace;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .stButton>button {
        background: linear-gradient(135deg, #ff6b6b, #ffa500);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: bold;
        padding: 8px 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #ffa500, #ff6b6b);
        transform: scale(1.05);
    }
    .total-box {
        background: linear-gradient(135deg, #28a745, #20c997);
        color: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ============ MENU DATA with Internet Images ============
MENU = {
    "🍕 Fast Food": {
        "Pizza": {"price": 1200, "img": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400"},
        "Burger": {"price": 650, "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400"},
        "French Fries": {"price": 350, "img": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=400"},
        "Hot Dog": {"price": 500, "img": "https://images.unsplash.com/photo-1612392062798-1e8a9b0dcb6e?w=400"},
        "Sandwich": {"price": 450, "img": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=400"},
        "Shawarma": {"price": 550, "img": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=400"},
        "Chicken Wings": {"price": 800, "img": "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?w=400"},
        "Nuggets": {"price": 600, "img": "https://images.unsplash.com/photo-1562967914-608f82629710?w=400"},
    },
    "🍛 Desi Food": {
        "Chicken Biryani": {"price": 450, "img": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400"},
        "Beef Karahi": {"price": 1500, "img": "https://images.unsplash.com/photo-1633945274405-b6c8069047b0?w=400"},
        "Chicken Tikka": {"price": 700, "img": "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=400"},
        "Nihari": {"price": 800, "img": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400"},
        "Haleem": {"price": 500, "img": "https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?w=400"},
        "Pulao": {"price": 400, "img": "https://images.unsplash.com/photo-1596797038530-2c107229654b?w=400"},
        "Seekh Kabab": {"price": 900, "img": "https://images.unsplash.com/photo-1603360946369-dc9bb6258143?w=400"},
        "Butter Chicken": {"price": 1300, "img": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400"},
    },
    "🍔 Burgers & Wraps": {
        "Zinger Burger": {"price": 750, "img": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=400"},
        "Beef Burger": {"price": 850, "img": "https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=400"},
        "Chicken Wrap": {"price": 550, "img": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400"},
        "Club Sandwich": {"price": 700, "img": "https://images.unsplash.com/photo-1567234669003-dce7a7a88821?w=400"},
    },
    "🍰 Desserts": {
        "Chocolate Cake": {"price": 400, "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400"},
        "Ice Cream": {"price": 300, "img": "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=400"},
        "Gulab Jamun": {"price": 250, "img": "https://images.unsplash.com/photo-1601303516534-bf0d5b1c2b5d?w=400"},
        "Kheer": {"price": 350, "img": "https://images.unsplash.com/photo-1582716401301-b2407dc7563d?w=400"},
        "Brownie": {"price": 450, "img": "https://images.unsplash.com/photo-1607920591413-4ec007e70023?w=400"},
    },
    "🥤 Drinks": {
        "Cold Drink": {"price": 150, "img": "https://images.unsplash.com/photo-1581636625402-29b2a704ef13?w=400"},
        "Fresh Juice": {"price": 250, "img": "https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=400"},
        "Lassi": {"price": 200, "img": "https://images.unsplash.com/photo-1626200419199-391ae4be7a41?w=400"},
        "Coffee": {"price": 300, "img": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=400"},
        "Tea": {"price": 100, "img": "https://images.unsplash.com/photo-1597318181409-cf64d0b5d8a2?w=400"},
        "Mint Margarita": {"price": 350, "img": "https://images.unsplash.com/photo-1546171753-97d7676e4602?w=400"},
    }
}

TAX_RATE = 0.05

# ============ SESSION STATE ============
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "order_count" not in st.session_state:
    st.session_state.order_count = 1000

# ============ HEADER ============
st.markdown("""
<div class="main-header">
    <h1>🍽️ HOTEL POS SYSTEM 🍔</h1>
    <p>✨ Fresh • Fast • Delicious — Order Now! ✨</p>
</div>
""", unsafe_allow_html=True)

# ============ SIDEBAR (Cart & Bill) ============
with st.sidebar:
    st.markdown("## 🛒 Your Cart")

    if not st.session_state.cart:
        st.info("Cart khali hai! Menu se items add karein.")
    else:
        for item, qty in list(st.session_state.cart.items()):
            if qty > 0:
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    price = 0
                    for cat, items in MENU.items():
                        if item in items:
                            price = items[item]["price"]
                            break
                    st.write(f"**{item}**")
                    st.caption(f"Rs {price} × {qty} = Rs {price*qty}")
                with col2:
                    if st.button("➕", key=f"inc_{item}"):
                        st.session_state.cart[item] += 1
                        st.rerun()
                with col3:
                    if st.button("➖", key=f"dec_{item}"):
                        st.session_state.cart[item] -= 1
                        if st.session_state.cart[item] <= 0:
                            del st.session_state.cart[item]
                        st.rerun()

        st.markdown("---")

        subtotal = 0
        for item, qty in st.session_state.cart.items():
            for cat, items in MENU.items():
                if item in items:
                    subtotal += items[item]["price"] * qty
                    break

        tax = subtotal * TAX_RATE
        total = subtotal + tax

        st.markdown(f"""
        <div class="bill-box">
            <p>Subtotal: <b>Rs {subtotal:,.0f}</b></p>
            <p>GST (5%): <b>Rs {tax:,.0f}</b></p>
            <hr>
            <p style="font-size:20px;">TOTAL: <b>Rs {total:,.0f}</b></p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        if st.button("🗑️ Clear Cart", use_container_width=True):
            st.session_state.cart = {}
            st.rerun()

# ============ MAIN TABS ============
tab1, tab2, tab3 = st.tabs(["📖 Menu", "🧾 Print Bill", "ℹ️ About"])

# ============ TAB 1: MENU ============
with tab1:
    st.markdown("### 🍴 Explore Our Delicious Menu")
    st.write("Apne pasandida khane par **'Add to Cart'** button dabayein.")

    for category, items in MENU.items():
        st.markdown(f'<div class="category-title">{category}</div>', unsafe_allow_html=True)

        cols = st.columns(4)
        for idx, (item_name, details) in enumerate(items.items()):
            with cols[idx % 4]:
                st.markdown('<div class="food-card">', unsafe_allow_html=True)
                try:
                    st.image(details["img"], use_container_width=True)
                except Exception:
                    st.write("🍽️")
                st.markdown(f"**{item_name}**")
                st.markdown(f'<span class="price-tag">Rs {details["price"]}</span>', unsafe_allow_html=True)

                if st.button(f"➕ Add", key=f"add_{category}_{item_name}", use_container_width=True):
                    if item_name in st.session_state.cart:
                        st.session_state.cart[item_name] += 1
                    else:
                        st.session_state.cart[item_name] = 1
                    st.success(f"✅ {item_name} added!")
                    st.rerun()

                st.markdown('</div>', unsafe_allow_html=True)

# ============ TAB 2: PRINT BILL ============
with tab2:
    st.markdown("### 🧾 Generate & Print Bill")

    if not st.session_state.cart:
        st.warning("⚠️ Cart khali hai! Pehle menu se items add karein.")
    else:
        col1, col2 = st.columns([1, 1])

        with col1:
            customer_name = st.text_input("👤 Customer Name", value="Walk-in Customer")
            table_no = st.text_input("🪑 Table Number", value="01")
            payment_mode = st.selectbox("💳 Payment Mode", ["Cash", "Card", "Easypaisa", "JazzCash"])
            order_type = st.radio("📦 Order Type", ["Dine-in", "Takeaway", "Delivery"], horizontal=True)

        with col2:
            st.markdown("#### 📋 Order Summary")
            subtotal = 0
            for item, qty in st.session_state.cart.items():
                for cat, items in MENU.items():
                    if item in items:
                        line_total = items[item]["price"] * qty
                        subtotal += line_total
                        st.write(f"• {item} × {qty} = Rs {line_total:,.0f}")
                        break

            tax = subtotal * TAX_RATE
            total = subtotal + tax
            st.markdown(f"**Subtotal:** Rs {subtotal:,.0f}")
            st.markdown(f"**GST (5%):** Rs {tax:,.0f}")
            st.markdown(f"### 💰 Total: Rs {total:,.0f}")

        st.markdown("---")

        if st.button("🖨️ Generate Bill", use_container_width=True):
            st.session_state.order_count += 1
            order_id = f"ORD-{st.session_state.order_count}"
            now = datetime.now().strftime("%d-%m-%Y  %I:%M %p")

            items_html = ""
            for item, qty in st.session_state.cart.items():
                for cat, items in MENU.items():
                    if item in items:
                        line_total = items[item]["price"] * qty
                        items_html += f"<tr><td>{item}</td><td style='text-align:center;'>{qty}</td><td style='text-align:right;'>Rs {items[item]['price']}</td><td style='text-align:right;'>Rs {line_total:,.0f}</td></tr>"
                        break

            receipt = f"""
            <div class="receipt">
                <div style="text-align:center;">
                    <h1 style="margin:0; color:#ff6b6b;">🍽️ HOTEL POS</h1>
                    <p style="margin:5px 0;">Taste of Excellence</p>
                    <p style="margin:5px 0; font-size:12px;">Main Boulevard, Lahore | Ph: 0300-1234567</p>
                    <hr style="border:1px dashed #333;">
                </div>
                <p><b>Order ID:</b> {order_id}</p>
                <p><b>Date:</b> {now}</p>
                <p><b>Customer:</b> {customer_name}</p>
                <p><b>Table #:</b> {table_no} | <b>Type:</b> {order_type}</p>
                <hr style="border:1px dashed #333;">
                <table style="width:100%; font-size:13px;">
                    <tr style="background:#ffe6cc;">
                        <th style="text-align:left;">Item</th>
                        <th>Qty</th>
                        <th style="text-align:right;">Price</th>
                        <th style="text-align:right;">Amount</th>
                    </tr>
                    {items_html}
                </table>
                <hr style="border:1px dashed #333;">
                <table style="width:100%;">
                    <tr><td>Subtotal:</td><td style="text-align:right;">Rs {subtotal:,.0f}</td></tr>
                    <tr><td>GST (5%):</td><td style="text-align:right;">Rs {tax:,.0f}</td></tr>
                    <tr style="font-size:18px; font-weight:bold; color:#28a745;">
                        <td>GRAND TOTAL:</td><td style="text-align:right;">Rs {total:,.0f}</td>
                    </tr>
                </table>
                <hr style="border:1px dashed #333;">
                <p><b>Payment Mode:</b> {payment_mode}</p>
                <div style="text-align:center; margin-top:20px;">
                    <p style="font-size:14px;">🙏 Thank you for dining with us!</p>
                    <p style="font-size:12px;">Visit again • Feedback: 0300-1234567</p>
                    <p style="font-size:11px;">*** Powered by Hotel POS System ***</p>
                </div>
            </div>
            """
            st.markdown(receipt, unsafe_allow_html=True)
            st.balloons()
            st.success(f"✅ Bill Generated Successfully! Order ID: {order_id}")

            receipt_text = f"""
========================================
        HOTEL POS - RECEIPT
========================================
Order ID   : {order_id}
Date       : {now}
Customer   : {customer_name}
Table No   : {table_no}
Order Type : {order_type}
----------------------------------------
ITEM                 QTY    PRICE    AMOUNT
----------------------------------------
"""
            for item, qty in st.session_state.cart.items():
                for cat, items in MENU.items():
                    if item in items:
                        p = items[item]["price"]
                        receipt_text += f"{item[:18]:20} {qty:3}   {p:6}   {p*qty:8}\n"
                        break

            receipt_text += f"""
----------------------------------------
Subtotal : Rs {subtotal:,.0f}
GST (5%) : Rs {tax:,.0f}
TOTAL    : Rs {total:,.0f}
----------------------------------------
Payment  : {payment_mode}
========================================
    Thank you! Visit Again!
========================================
"""

            st.download_button(
                "📥 Download Receipt (.txt)",
                receipt_text,
                file_name=f"{order_id}.txt",
                mime="text/plain",
                use_container_width=True
            )

# ============ TAB 3: ABOUT ============
with tab3:
    st.markdown("### ℹ️ About This POS System")
    st.markdown("""
    <div class="bill-box">
        <h3>🍽️ Hotel POS Web Application</h3>
        <p><b>Version:</b> 1.0.0</p>
        <p><b>Developed in:</b> Pure Python (Streamlit)</p>
        <p><b>Features:</b></p>
        <ul>
            <li>✅ Complete Food Menu with Images</li>
            <li>✅ 5 Categories (Fast Food, Desi, Burgers, Desserts, Drinks)</li>
            <li>✅ 30+ Food Items with Prices</li>
            <li>✅ Add/Remove Items from Cart</li>
            <li>✅ Live Bill Calculation</li>
            <li>✅ 5% GST Tax Calculation</li>
            <li>✅ Professional Receipt Generation</li>
            <li>✅ Download Receipt as Text File</li>
            <li>✅ Customer Name & Table Number</li>
            <li>✅ Multiple Payment Modes</li>
            <li>✅ Beautiful Gradient UI</li>
            <li>✅ Responsive Design</li>
        </ul>
        <p><b>Technology:</b> Python + Streamlit + HTML/CSS</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📊 Statistics")
    total_items = sum(len(items) for items in MENU.values())
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🍽️ Total Items", total_items)
    col2.metric("📂 Categories", len(MENU))
    col3.metric("🛒 Cart Items", sum(st.session_state.cart.values()) if st.session_state.cart else 0)
    col4.metric("💰 Tax Rate", "5%")

# ============ FOOTER ============
st.markdown("---")
st.caption("🍽️ Hotel POS System • Built with Python + Streamlit")
