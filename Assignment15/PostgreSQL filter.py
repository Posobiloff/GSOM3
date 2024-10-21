# Connection establishment
%load_ext sql
import os
USER = os.environ['POSTGRESQL_USER']
PASSWORD = os.environ['POSTGRESQL_PASSWORD']
POSTGRESQL_HOST = '10.129.0.25'
DBASE_NAME = 'demo'
CONNECT_DATA = 'postgresql://{}:{}@{}/{}'.format(
    USER,
    PASSWORD,
    POSTGRESQL_HOST,
    DBASE_NAME
)

%%sql $CONNECT_DATA
SELECT ticket_no,
departure_airport, 
airport_name as departure_airport_name,
city as departure_airport_city,
arrival_airport
FROM Airports 
JOIN 
   (SELECT departure_airport, arrival_airport, ticket_no 
    FROM Flights 
    JOIN Ticket_flights 
    ON Ticket_flights.flight_id = Flights.flight_id) as t 
ON t.departure_airport = Airports.airport_code 
WHERE ticket_no = '0005432312164'


%%sql $CONNECT_DATA
SELECT ticket_no,
s.departure_airport, 
s.departure_airport_name,
s.departure_airport_city,
s.arrival_airport,
airport_name as arrival_airport_name,
city as arrival_airport_city
FROM Airports
JOIN
    (SELECT ticket_no,
     departure_airport, 
     airport_name as departure_airport_name,
     city as departure_airport_city,
     arrival_airport
     FROM Airports 
     JOIN 
        (SELECT departure_airport, arrival_airport, ticket_no 
         FROM Flights 
         JOIN Ticket_flights 
         ON Ticket_flights.flight_id = Flights.flight_id) as t 
      ON t.departure_airport = Airports.airport_code 
      WHERE ticket_no = '0005432312164') as s
ON s.arrival_airport = Airports.airport_code 

%%sql $CONNECT_DATA
    SELECT passenger_id, 
    passenger_name, 
    Tickets.ticket_no, 
    info.departure_airport,
    info.departure_airport_name,
    info.departure_airport_city,
    info.arrival_airport,
    info.arrival_airport_name,
    info.arrival_airport_city
    FROM Tickets 
    JOIN
        (SELECT ticket_no,
        s.departure_airport, 
        s.departure_airport_name,
        s.departure_airport_city,
        s.arrival_airport,
        airport_name as arrival_airport_name,
        city as arrival_airport_city
        FROM Airports
        JOIN
            (SELECT ticket_no,
             departure_airport, 
             airport_name as departure_airport_name,
             city as departure_airport_city,
             arrival_airport
             FROM Airports 
             JOIN 
                (SELECT departure_airport, arrival_airport, ticket_no 
                 FROM Flights 
                 JOIN Ticket_flights 
                 ON Ticket_flights.flight_id = Flights.flight_id) as t 
              ON t.departure_airport = Airports.airport_code 
              WHERE ticket_no = '0005432312164') as s
        ON s.arrival_airport = Airports.airport_code) as info
    ON Tickets.ticket_no = info.ticket_no 
    
    