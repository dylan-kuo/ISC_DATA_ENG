# ISC Data Engineering Assessment

## Exercise 1: Data Modeling/SQL
&nbsp;

### a. Design Considerations
- Building: The building where the elevators belong to. It consists of building_id (primary key), building_name, and the address. 

- Elevator: Each elevator installed in the building. It constits of elevator_id (primary key), building_id (foreign key referencing Building), status that signifies out of service or in srevice.

- Trip: Each trip made by the elevator and the passenger. It consists trip_id (primary key), elevator_id (foreign key referencing Elevator), start_time, end_time, start_floor, end_floor.

- Passenger: Each Passenger who requested a trip. It consists of passenger_id (primary key), passenger_name.

- PassengerTrip: The bridging table between Passenger and Trip for the many-to-many relationship implementation (ie, one passenger can have multiple trips. one trip can involve multiple passenger). It consists of passenger_id (foreign key referencing Passenger), trip_id (foreign key referencing Trip), request_time. The combincation of passenger_id and trip_id acts as a composite key.


### b. Assumptions 

- The elevator system only records the start and end floors when a passenger requests a trip. Information about intermediate floors is not captured to simplify the logic.

- The direction of the elevator (i.e., up or down) is not recorded. It can be inferred from the start and end floors.

- The elevator is assumed to have no capacity limitation, and the number of passengers on the same elevator is not recorded.

### Sql Queries for Metrics

1.  Total number of passengers per day
  
    ```
    SELECT date(start_time) AS date, COUNT(distinct passenger_id) AS total_passengers
    FROM trip
    JOIN PassengerTrip ON trip.trip_id = PassengerTrip.trip_id
    GROUP by date(start_time)
    ```

2.  Total number of trips per day
  
    ```
    SELECT count(*) AS total_trips
    FROM Trip
    ```

3.  Average number of passengers per trip
  
     ```
     SELECT COUNT(distinct passenger_id)/COUNT(distinct trip_id) AS avg_passengers_per_trip
     FROM Trip
     JOIN PassengerTrip ON Trip.trip_id = PassengerTrip.trip_id
     ```

4.  Average wait time for passengers
  
    ```
    SELECT AVG(start_time - request_time) AS avg_wait_time
    FROM Trip t
    JOIN PassengerTrip ON Trip.trip_id = PassengerTrip.trip_id
    ```

5.  Average travel time per trip
  
    ```
    SELECT AVG(end_time - start_time) AS avg_travel_time
    FROM Trip
    ```

6.  Busiest times of the day/week for the elevator system
  
    ```
    SELECT DATE_PART('hour', start_time) AS hour_of_day, DATE_PART('dow', start_time) AS day_of_week, COUNT(trip_id) AS total_trips
    FROM Trip
    GROUP BY HOUR(start_time), DAYOFWEEK(start_time)
    ORDER BY COUNT(trip_id) DESC;
    ```

&nbsp;

## Exercise 2: Software Design/Coding
&nbsp;
