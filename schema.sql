create table chat_room
(
	id serial not null
		constraint chat_room_pkey
			primary key,
	created_at timestamp,
	updated_at timestamp,
	name varchar
);

create table "user"
(
	id serial not null
		constraint user_pkey
			primary key,
	created_at timestamp,
	updated_at timestamp,
	email varchar,
	username varchar,
	password varchar
);

create table message
(
	id serial not null
		constraint message_pkey
			primary key,
	created_at timestamp,
	updated_at timestamp,
	user_id integer not null
		constraint message_user_id_fkey
			references "user",
	content varchar,
	room_id integer
		constraint message_room_id_fkey
			references chat_room,
	recipient_id integer
		constraint message_recipient_id_fkey
			references "user"
);

