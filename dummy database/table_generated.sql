CREATE TABLE public.generatedpeople
(
   "DM_month" integer,
   "DM_day" integer,
   "DM_year" integer,
   "Age" integer,
   "Name" character varying(100), -- in case if any name like Ovuvuevuevue Onyetenyevwe Ugwemubwem Ossas will appear
   "College" character varying(20),
   "Sex" character varying(20),
   "Skin_Colour" character varying(20),
   "Eye_Colour" character varying(20),
   "Hair_Colour" character varying(20),
   -- all of the following measurement should be stored in mm
   "Head_length" integer, 
   "Face_breadth" integer,
   "Face_iobreadth" integer, --interocular length
   id serial NOT NULL, --no need to generate as this field will be automatically generated upon import
   CONSTRAINT generatedpeoplestudentkey PRIMARY KEY (id)
)
