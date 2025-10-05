import pandas as pd
from sqlalchemy import create_engine
import warnings

user_data = {
    'user_id': [1, 2, 3, 4, 5],
    'full_name': ['Alice Smith', 'Bob Johnson', 'Charlie Lee', 'David Brown', 'Eva White'],
    'phone_number': ['123-456-7890', '234-567-8901', '345-678-9012', '456-789-0123', '567-890-1234'],
}

artis_data = {
    'artist_id': [1, 2, 3, 4, 5],
    'artist_name': ['The Beatles', 'Elvis Presley', 'Michael Jackson', 'Madonna', 'Queen'],
    'genre': ['Rock', 'Rock and Roll', 'Pop', 'Pop', 'Rock']
}

venue_data = {
    'venue_id': [1, 2, 3, 4, 5],
    'venue_name': ['Madison Square Garden', 'The O2 Arena', 'Sydney Opera House', 'Wembley Stadium', 'Hollywood Bowl'],
    'location': ['New York, USA', 'London, UK', 'Sydney, Australia', 'London, UK', 'Los Angeles, USA'],
    'kapasitas': [20000, 20000, 5700, 90000, 17500]
}

event_data = {
    'event_id': [1, 2, 3, 4, 5],
    'event_name': ['Rock Concert', 'Pop Festival', 'Jazz Night', 'Classical Evening', 'Hip Hop Bash'],
    'event_date': ['2023-10-01', '2023-11-15', '2023-12-05', '2024-01-20', '2024-02-14'],
    'venue_id': [1, 2, 3, 4, 5],
    'artist_id': [1, 4, 3, 2, 5]
}

tickettier_data = {
    'tickettier_id': [1, 2, 3, 4, 5],
    'tiername': ['VVIP', 'VIP', 'Side', 'Balcony' , 'Regular'],
    'price': [200.00, 150.00, 100.00, 75.00, 50.00],
    'quota': [100, 150, 300, 400, 500]
} 

booking_data = {
    'booking_id': [1, 2, 3, 4, 5],
    'user_id': [1, 2, 3, 4, 5],
    'ticket_id': [1, 2, 3, 4, 5],
    'booking_date': ['2023-09-01', '2023-09-15', '2023-10-05', '2023-11-20', '2023-12-14']
}

ticket_data = {
    'ticket_id': [1, 2, 3, 4, 5],
    'booking_id': [1, 2, 3, 4, 5],
    'tickettier_id': [1, 2, 3, 4, 5],
    'ticket_code': ['TCKT001', 'TCKT002', 'TCKT003', 'TCKT004', 'TCKT005'],
    'status': ['true', 'true', 'false', 'true', 'false']
}

payment_data = {
    'payment_id': [1, 2, 3, 4, 5],
    'booking_id': [1, 2, 3, 4, 5],
    'payment_method': ['Credit Card', 'PayPal', 'Bank Transfer', 'Credit Card', 'PayPal'],
    'status': ['completed', 'completed', 'pending', 'completed', 'failed']
}

promotion_data = {
    'promotion_id': [1, 2, 3, 4, 5],
    'promo_code': ['ROCK10', 'POP20', 'JAZZ15', 'CLASSICAL5', 'HIPHOP25'],
    'discount_percentage': [10, 20, 15, 5, 25],
    'valid_until': ['2023-12-31', '2023-11-30', '2023-10-31', '2024-01-31', '2023-12-15']
}

eventorganizer_data = {
    'eventorganizer_id': [1, 2, 3, 4, 5],
    'organizer_name': ['Live Nation', 'AEG Presents', 'Eventbrite', 'Ticketmaster', 'Cvent'],
    'contact_info': ['a@gmail.com', 'b@gmail.com', 'c@gmail.com', 'd@gmail.com', 'e@gmail.com']
}

seat_data = {
    'seat_id': [1, 2, 3, 4, 5],
    'venue_id': [1, 1, 2, 2, 3],
    'seat_number': ['A1', 'A2', 'B1', 'B2', 'C1']
}
