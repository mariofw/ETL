
const fs = require('fs');
const path = require('path');

const toRowObjects = (data) => {
    const keys = Object.keys(data);
    const rows = [];
    for (let i = 0; i < data[keys[0]].length; i++) {
        let row = {};
        for (const key of keys) {
            row[key] = data[key][i];
        }
        rows.push(row);
    }
    return rows;
};

console.log('Running ETL...');

try {
    const rawData = fs.readFileSync(path.join(__dirname, 'oltp_data.json'), 'utf-8');
    const oltp = JSON.parse(rawData);

    const users = toRowObjects(oltp.users);
    const artists = toRowObjects(oltp.artists);
    const venues = toRowObjects(oltp.venues);
    const events = toRowObjects(oltp.events);
    const tiers = toRowObjects(oltp.ticket_tiers);
    const bookings = toRowObjects(oltp.bookings);
    const tickets = toRowObjects(oltp.tickets);
    const payments = toRowObjects(oltp.payments);
    const promotions = toRowObjects(oltp.promotions);
    const eventOrganizers = toRowObjects(oltp.event_organizers);
    const seats = toRowObjects(oltp.seats);

    const dataWarehouse = bookings.map(booking => {
        const user = users.find(u => u.user_id === booking.user_id);
        const payment = payments.find(p => p.booking_id === booking.booking_id);
        const ticket = tickets.find(t => t.ticket_id === booking.ticket_id);
        
        const tier = ticket ? tiers.find(ti => ti.tickettier_id === ticket.tickettier_id) : null;
        const event = ticket ? events.find(e => e.event_id === ticket.tickettier_id) : null; // Assumption

        const artist = event ? artists.find(a => a.artist_id === event.artist_id) : null;
        const venue = event ? venues.find(v => v.venue_id === event.venue_id) : null;
        const promotion = ticket ? promotions.find(p => p.promotion_id === ticket.tickettier_id) : null;
        const eventOrganizer = event ? eventOrganizers.find(eo => eo.eventorganizer_id === event.artist_id) : null;
        const seat = ticket ? seats.find(s => s.seat_id === ticket.tickettier_id) : null;

        return {
            booking_id: booking.booking_id,
            booking_date: booking.booking_date,
            user: {
                full_name: user?.full_name,
                phone_number: user?.phone_number
            },
            payment: {
                payment_method: payment?.payment_method,
                status: payment?.status
            },
            ticket: {
                ticket_code: ticket?.ticket_code,
                status: ticket?.status,
                tier_name: tier?.tiername,
                price: tier?.price,
                promotion: {
                    promo_code: promotion?.promo_code,
                    discount_percentage: promotion?.discount_percentage
                }
            },
            event: {
                event_name: event?.event_name,
                event_date: event?.event_date,
                artist_name: artist?.artist_name,
                genre: artist?.genre,
                venue_name: venue?.venue_name,
                location: venue?.location,
                organizer_name: eventOrganizer?.organizer_name,
                seat: {
                    seat_number: seat?.seat_number
                }
            }
        };
    });

    fs.writeFileSync(path.join(__dirname, 'data_warehouse.json'), JSON.stringify(dataWarehouse, null, 2));

    console.log('ETL process finished. Output: data_warehouse.json');

} catch (error) {
    console.error('ETL failed:', error);
}
