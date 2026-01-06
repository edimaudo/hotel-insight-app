from utils import *
from data import *

st.title(APP_NAME)
st.header(DASHBOARD_HEADER)


with st.sidebar:
    month_option = st.multiselect("Month", month_list,default=month_list)
    room_type_option = st.multiselect("Room Type",room_type_list, default=room_type_list)
    request_type_option = st.multiselect("Room Request",request_type_list, default=request_type_list)

# load intgrated df * filter
integrated_bookings_df2 = integrated_bookings_df[
    (integrated_bookings_df['booking_month'].isin(month_option)) & 
    (integrated_bookings_df['room type'].isin(room_type_option)) & 
    (integrated_bookings_df['request type'].isin(request_type_option))
]

integrated_bookings_df2['booking_revenue'] = integrated_bookings_df2['stay_duration'] * integrated_bookings_df2['price/day']
total_room_nights_sold = integrated_bookings_df2['stay_duration'].sum()
min_start_date = integrated_bookings_df2['start date_x'].min()
max_end_date = integrated_bookings_df2['end date_x'].max()
total_days_in_period = (max_end_date - min_start_date).days + 1
total_unique_rooms = integrated_bookings_df2['room'].nunique()
total_available_room_nights = total_unique_rooms * total_days_in_period
occupancy_rate = total_room_nights_sold / total_available_room_nights
print(f"Occupancy Rate: {occupancy_rate:.2%}")
adr = integrated_bookings_df2['booking_revenue'].sum() / total_room_nights_sold
print(f"Average Daily Rate (ADR): ${adr:.2f}")
revpar = integrated_bookings_df2['booking_revenue'].sum() / total_available_room_nights
print(f"Revenue Per Available Room (RevPAR): ${revpar:.2f}")
#print("--- Calculating Average Food Order Value ---")
#average_food_order_value = integrated_food_orders_df['order_value'].sum() / len(integrated_food_orders_df)
#print(f"Average Food Order Value: ${average_food_order_value:.2f}")
total_requests = requests_df['request id'].nunique()
fulfilled_requests = bookings_df['request id'].nunique()
request_fulfillment_rate = fulfilled_requests / total_requests
print(f"Request Fulfillment Rate: {request_fulfillment_rate:.2%}")
average_length_of_stay = integrated_bookings_df2['stay_duration'].mean()
print(f"Average Length of Stay: {average_length_of_stay:.2f} days")



st.subheader("KPIs")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Occupancy Rate", value=f"{occupancy_rate:.2%}")
with col2:
    st.metric(label="Average Daily Rate (ADR)", value="70 °F", )
with col3:
    st.metric(label="Revenue Per Available Room (RevPAR)", value="70 °F", delta="1.2 °F")
with col4:
    st.metric(label="Average Length of Stay", value="70 °F", delta="1.2 °F")

tab1, tab2, tab3, tab4 = st.tabs(["Booking",'Request Type', "Room Type", "Food"])

with tab1:
    st.subheader("Booking Trends")

with tab2:
    st.subheader("Request Trends")

with tab3:
    st.subheader("Room Type Trends")

with tab4:
    st.subheader("Food & Beverage Trends")


