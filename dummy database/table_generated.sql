CREATE TABLE public.generatedpeople
(
   "DoB_month" integer, --date of birth
   "DoB_day" integer,
   "DoB_year" integer,
   "Age" integer,
   "Name" character varying(100), -- in case if any name like Ovuvuevuevue Onyetenyevwe Ugwemubwem Ossas will appear
   "College" character varying(20),
   "Sex" character varying(20),
   "Eye_Colour" character varying(20),
   "Hair_Colour" character varying(20),
   -- all of the following measurement should be stored in cm
   "Head_length" real, 
   "Face_breadth" real,
   "Face_iobreadth" real, --interocular length
   id serial NOT NULL, --no need to generate as this field will be automatically generated upon import
   CONSTRAINT generatedpeoplestudentkey PRIMARY KEY (id)
)
