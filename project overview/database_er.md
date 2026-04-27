## ER Model

<img width="785" height="430" alt="er_diagram" src="https://github.com/user-attachments/assets/96581d05-f317-42e7-b6e7-98f2aff8a5bc" />

This ER diagram represents a global weather and climate analytics database. The system stores geographic locations, weather stations, measurement types, daily recorded measurements, and user interactions.

This includes:

- Strong entities (Location, WeatherStation, MeasurementType, User, StationMetadata)

- A weak entity (DailyMeasurement), identified by the composite key (StationID, TypeID, MeasurementDate)

- An associative entity (UserQuery) to resolve the many-to-many relationship between User and MeasurementType

----------

The diagram demonstrates:

One-to-many relationships (Location - > WeatherStation, WeatherStation → DailyMeasurement)

A one-to-one relationship (WeatherStation < - > StationMetadata)

A many-to-many relationship (User < - > MeasurementType via UserQuery)

----------

User Groups

- Admin

- Researchers

- Students

- Viewers
