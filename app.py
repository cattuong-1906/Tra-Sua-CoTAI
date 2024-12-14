import streamlit as st

def create_interface():
    st.title('Trà Sữa CoTAI')

    col1, col2 = st.columns(2)
    with col1:
        st.image('https://imgur.com/lEpdPsT.png')
    with col2:
        size = st.radio('Kích cỡ', ('Nhỏ (30K)', 'Vừa (40K)', 'Lớn (50K)'), horizontal = True)
        st.write('Thêm')
        col3, col4 = st.columns(2)
        with col3:
            milk = st.checkbox('Sữa (5K)')
            coffee = st.checkbox('Cà phê (8K)')
        with col4:
            cream = st.checkbox('Kem (10K)')
            egg = st.checkbox('Trứng (15K)')

    col5, col6 = st.columns(2)
    with col5:
        topping = st.multiselect('Topping', ['Trân châu trắng (5K)', 
                                     'Trân châu đen (5K)', 
                                     'Thạch rau câu (6K)',
                                     'Vải (7K)',
                                     'Nhãn (8K)',
                                     'Đào (10K)'])
    with col6:
        quantity = st.number_input('Số lượng', 0)

    note = st.text_area('Ghi chú', 'Ít đá, nhiều sữa')

    return size, milk, coffee, cream, egg, topping, quantity, note


def calculate(size, milk, coffee, cream, egg, topping, quantity):
    size_price = 0
    if size == 'Nhỏ (30K)':
        size_price = 30
    elif size == 'Vừa (40K)':
        size_price = 40
    elif size == 'Lớn (50K)':
        size_price = 50

    add_price = 0
    add = []
    if milk == True:
        add_price = add_price + 5
        add.append('Sữa')
    if coffee == True:
        add_price = add_price + 8
        add.append('Cà phê')
    if cream == True:
        add_price = add_price + 10
        add.append('Kem')
    if egg == True:
        add_price == add_price + 15
        add.append('Trứng')
        

    topping_price = 0
    for i in topping:
        if i == 'Trân châu trắng (5K)':
            topping_price = topping_price + 5
        if i == 'Trân châu đen (5K)':
            topping_price = topping_price + 5
        if i == 'Thạch rau câu (6K)':
            topping_price = topping_price + 6
        if i == 'Vải (7K)':
            topping_price = topping_price + 7
        if i == 'Nhãn (8K)':
            topping_price = topping_price + 8
        if i == 'Đào (10K)':
            topping_price = topping_price + 10

    total = (size_price + add_price + topping_price) * quantity

    return total, add

def main():
    size, milk, coffee, cream, egg, topping, quantity, note = create_interface()
    total, add = calculate(size, milk, coffee, cream, egg, topping, quantity)
    if st.button('Đặt hàng', use_container_width=True):
        #st.success(f'Cỡ: {size[:-5]}')
        #st.success(f'Thêm: {add}') 
        #st.success(f'Topping: {", ".join(topping)}')
        #st.success(note)
        #st.success(f'Thành tiền: {int(total)}K')
        #st.success('Cỡ: \nThêm:')    
        st.markdown(f"""
        <div style="color: green; background-color: #dff0d8; padding: 10px; border-radius: 5px;">
            Cỡ: {size[:-5]}<br>
            Thêm: {", ".join(add)}<br>
            Topping: {", ".join(topping)}<br>
            {note}<br>
            Thành tiền: {int(total)}K
        </div>
        """, unsafe_allow_html=True)     

main()




