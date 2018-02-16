CREATE TABLE public.generatedpeople
(
   "DM_month" integer,
   "DM_day" integer,
   "DM_year" integer,
   "Name" character varying(100), -- in case if any name like Ovuvuevuevue Onyetenyevwe Ugwemubwem Ossas will appear
   "College" character varying(20),
   "Age" integer,
   "Birthplace1" character varying(100), -- in case if any place like Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu will appear
   "Birthplace2" character varying(100),
   "Father_origin" character varying(100),
   "Mother_origin" character varying(100),
   "Skin" character varying(20),
   "Hair_colour" character varying(20),
   "Eyes" character varying(20), -- light, medium, or dark
   "Hair_type" character varying(20),
   "Head_length" integer, -- all of the following measurement should be stored in mm
   "Head_breadth" integer,
   "Head_height" integer,
   "Face_breadth" integer,
   "Face_iobreadth" integer,
   id serial NOT NULL,
   CONSTRAINT generatedpeoplestudentkey PRIMARY KEY (id)
)
