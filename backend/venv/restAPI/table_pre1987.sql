CREATE TABLE public.students_pre_1897
(
   "Name" character varying(100), 	-- in case if any name like Ovuvuevuevue Onyetenyevwe Ugwemubwem Ossas will appear
   "College" character varying(30),
   "Birthplace1" character varying(100), -- in case if any place like Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu will appear
   "Birthplace2" character varying(100),
   "DB_month" integer, -- Date of birth
   "DB_day" integer,
   "DB_year" integer,
   "Origin1" character varying(100),
   "Origin2" character varying(100),
   "Age" integer,
   "DM_month" integer,
   "DM_day" integer,
   "DM_year" integer,
   "Initials" character varying(20),
   "Eyes" integer, -- light, medium, or dark
   "Eye_right" integer, --eyesight for left
   "Eye_left" integer, --eyesight for right
   "Pull_archer" integer, 
   "Squeeze_right" integer,
   "Squeeze_left" integer,
   "Breathing Power" integer, -- cubic inches
   "Head (annotation in box)" real,
   "Head_breadth" real,
   "Head_length" real,
   "Head_brow" real, -- above te line from brow to ear-hole
   "Height_feet" real,
   "Height_inches" integer,
   "Height_tenths" integer,
   "Heel_inches" integer,
   "Heel_tenths" integer,
   "True_feet" integer, -- true height
   "True_inches" integer,
   "True_tenths" integer,
   "Weight_stone" integer,
   "Weight_lbs" real,	
   "Weight_oz (rare)" real,
   "Span_ft" real,
   "Span_in" real,
   "Span_tenths" real,
   id serial NOT NULL,
   CONSTRAINT pre1897studentkey PRIMARY KEY (id)
)
