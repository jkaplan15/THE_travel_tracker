#!/usr/bin/env python3

from app import app
from models import db, User, Country, Trip
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # List of countries
    country_data = [
        {"country_name": "Afghanistan", "country_code": "af", "country_image": "https://flagcdn.com/w80/af.png"},
        {"country_name": "Albania", "country_code": "al", "country_image": "https://flagcdn.com/w80/al.png"},
        {"country_name": "Algeria", "country_code": "dz", "country_image": "https://flagcdn.com/w80/dz.png"},
        {"country_name": "Andorra", "country_code": "ad", "country_image": "https://flagcdn.com/w80/ad.png"},
        {"country_name": "Angola", "country_code": "ao", "country_image": "https://flagcdn.com/w80/ao.png"},
        {"country_name": "Antigua and Barbuda", "country_code": "ag", "country_image": "https://flagcdn.com/w80/ag.png"},
        {"country_name": "Argentina", "country_code": "ar", "country_image": "https://flagcdn.com/w80/ar.png"},
        {"country_name": "Armenia", "country_code": "am", "country_image": "https://flagcdn.com/w80/am.png"},
        {"country_name": "Australia", "country_code": "au", "country_image": "https://flagcdn.com/w80/au.png"},
        {"country_name": "Austria", "country_code": "at", "country_image": "https://flagcdn.com/w80/at.png"},
        {"country_name": "Azerbaijan", "country_code": "az", "country_image": "https://flagcdn.com/w80/az.png"},
        {"country_name": "Bahamas", "country_code": "bs", "country_image": "https://flagcdn.com/w80/bs.png"},
        {"country_name": "Bahrain", "country_code": "bh", "country_image": "https://flagcdn.com/w80/bh.png"},
        {"country_name": "Bangladesh", "country_code": "bd", "country_image": "https://flagcdn.com/w80/bd.png"},
        {"country_name": "Barbados", "country_code": "bb", "country_image": "https://flagcdn.com/w80/bb.png"},
        {"country_name": "Belarus", "country_code": "by", "country_image": "https://flagcdn.com/w80/by.png"},
        {"country_name": "Belgium", "country_code": "be", "country_image": "https://flagcdn.com/w80/be.png"},
        {"country_name": "Belize", "country_code": "bz", "country_image": "https://flagcdn.com/w80/bz.png"},
        {"country_name": "Benin", "country_code": "bj", "country_image": "https://flagcdn.com/w80/bj.png"},
        {"country_name": "Bhutan", "country_code": "bt", "country_image": "https://flagcdn.com/w80/bt.png"},
        {"country_name": "Bolivia", "country_code": "bo", "country_image": "https://flagcdn.com/w80/bo.png"},
        {"country_name": "Bosnia and Herzegovina", "country_code": "ba", "country_image": "https://flagcdn.com/w80/ba.png"},
        {"country_name": "Botswana", "country_code": "bw", "country_image": "https://flagcdn.com/w80/bw.png"},
        {"country_name": "Brazil", "country_code": "br", "country_image": "https://flagcdn.com/w80/br.png"},
        {"country_name": "Brunei", "country_code": "bn", "country_image": "https://flagcdn.com/w80/bn.png"},
        {"country_name": "Bulgaria", "country_code": "bg", "country_image": "https://flagcdn.com/w80/bg.png"},
        {"country_name": "Burkina Faso", "country_code": "bf", "country_image": "https://flagcdn.com/w80/bf.png"},
        {"country_name": "Burundi", "country_code": "bi", "country_image": "https://flagcdn.com/w80/bi.png"},
        {"country_name": "Cabo Verde", "country_code": "cv", "country_image": "https://flagcdn.com/w80/cv.png"},
        {"country_name": "Cambodia", "country_code": "kh", "country_image": "https://flagcdn.com/w80/kh.png"},
        {"country_name": "Cameroon", "country_code": "cm", "country_image": "https://flagcdn.com/w80/cm.png"},
        {"country_name": "Canada", "country_code": "ca", "country_image": "https://flagcdn.com/w80/ca.png"},
        {"country_name": "Central African Republic", "country_code": "cf", "country_image": "https://flagcdn.com/w80/cf.png"},
        {"country_name": "Chad", "country_code": "td", "country_image": "https://flagcdn.com/w80/td.png"},
        {"country_name": "Chile", "country_code": "cl", "country_image": "https://flagcdn.com/w80/cl.png"},
        {"country_name": "China", "country_code": "cn", "country_image": "https://flagcdn.com/w80/cn.png"},
        {"country_name": "Colombia", "country_code": "co", "country_image": "https://flagcdn.com/w80/co.png"},
        {"country_name": "Comoros", "country_code": "km", "country_image": "https://flagcdn.com/w80/km.png"},
        {"country_name": "Congo", "country_code": "cg", "country_image": "https://flagcdn.com/w80/cg.png"},
        {"country_name": "Costa Rica", "country_code": "cr", "country_image": "https://flagcdn.com/w80/cr.png"},
        {"country_name": "Croatia", "country_code": "hr", "country_image": "https://flagcdn.com/w80/hr.png"},
        {"country_name": "Cuba", "country_code": "cu", "country_image": "https://flagcdn.com/w80/cu.png"},
        {"country_name": "Cyprus", "country_code": "cy", "country_image": "https://flagcdn.com/w80/cy.png"},
        {"country_name": "Czechia", "country_code": "cz", "country_image": "https://flagcdn.com/w80/cz.png"},
        {"country_name": "Denmark", "country_code": "dk", "country_image": "https://flagcdn.com/w80/dk.png"},
        {"country_name": "Djibouti", "country_code": "dj", "country_image": "https://flagcdn.com/w80/dj.png"},
        {"country_name": "Dominica", "country_code": "dm", "country_image": "https://flagcdn.com/w80/dm.png"},
        {"country_name": "Dominican Republic", "country_code": "do", "country_image": "https://flagcdn.com/w80/do.png"},
        {"country_name": "East Timor", "country_code": "tl", "country_image": "https://flagcdn.com/w80/tl.png"},
        {"country_name": "Ecuador", "country_code": "ec", "country_image": "https://flagcdn.com/w80/ec.png"},
        {"country_name": "Egypt", "country_code": "eg", "country_image": "https://flagcdn.com/w80/eg.png"},
        {"country_name": "El Salvador", "country_code": "sv", "country_image": "https://flagcdn.com/w80/sv.png"},
        {"country_name": "Equatorial Guinea", "country_code": "gq", "country_image": "https://flagcdn.com/w80/gq.png"},
        {"country_name": "Eritrea", "country_code": "er", "country_image": "https://flagcdn.com/w80/er.png"},
        {"country_name": "Estonia", "country_code": "ee", "country_image": "https://flagcdn.com/w80/ee.png"},
        {"country_name": "Eswatini", "country_code": "sz", "country_image": "https://flagcdn.com/w80/sz.png"},
        {"country_name": "Ethiopia", "country_code": "et", "country_image": "https://flagcdn.com/w80/et.png"},
        {"country_name": "Fiji", "country_code": "fj", "country_image": "https://flagcdn.com/w80/fj.png"},
        {"country_name": "Finland", "country_code": "fi", "country_image": "https://flagcdn.com/w80/fi.png"},
        {"country_name": "France", "country_code": "fr", "country_image": "https://flagcdn.com/w80/fr.png"},
        {"country_name": "Gabon", "country_code": "ga", "country_image": "https://flagcdn.com/w80/ga.png"},
        {"country_name": "Gambia", "country_code": "gm", "country_image": "https://flagcdn.com/w80/gm.png"},
        {"country_name": "Georgia", "country_code": "ge", "country_image": "https://flagcdn.com/w80/ge.png"},
        {"country_name": "Germany", "country_code": "de", "country_image": "https://flagcdn.com/w80/de.png"},
        {"country_name": "Ghana", "country_code": "gh", "country_image": "https://flagcdn.com/w80/gh.png"},
        {"country_name": "Greece", "country_code": "gr", "country_image": "https://flagcdn.com/w80/gr.png"},
        {"country_name": "Grenada", "country_code": "gd", "country_image": "https://flagcdn.com/w80/gd.png"},
        {"country_name": "Guatemala", "country_code": "gt", "country_image": "https://flagcdn.com/w80/gt.png"},
        {"country_name": "Guinea", "country_code": "gn", "country_image": "https://flagcdn.com/w80/gn.png"},
        {"country_name": "Guinea-Bissau", "country_code": "gw", "country_image": "https://flagcdn.com/w80/gw.png"},
        {"country_name": "Guyana", "country_code": "gy", "country_image": "https://flagcdn.com/w80/gy.png"},
        {"country_name": "Haiti", "country_code": "ht", "country_image": "https://flagcdn.com/w80/ht.png"},
        {"country_name": "Honduras", "country_code": "hn", "country_image": "https://flagcdn.com/w80/hn.png"},
        {"country_name": "Hungary", "country_code": "hu", "country_image": "https://flagcdn.com/w80/hu.png"},
        {"country_name": "Iceland", "country_code": "is", "country_image": "https://flagcdn.com/w80/is.png"},
        {"country_name": "India", "country_code": "in", "country_image": "https://flagcdn.com/w80/in.png"},
        {"country_name": "Indonesia", "country_code": "id", "country_image": "https://flagcdn.com/w80/id.png"},
        {"country_name": "Iran", "country_code": "ir", "country_image": "https://flagcdn.com/w80/ir.png"},
        {"country_name": "Iraq", "country_code": "iq", "country_image": "https://flagcdn.com/w80/iq.png"},
        {"country_name": "Ireland", "country_code": "ie", "country_image": "https://flagcdn.com/w80/ie.png"},
        {"country_name": "Israel", "country_code": "il", "country_image": "https://flagcdn.com/w80/il.png"},
        {"country_name": "Italy", "country_code": "it", "country_image": "https://flagcdn.com/w80/it.png"},
        {"country_name": "Jamaica", "country_code": "jm", "country_image": "https://flagcdn.com/w80/jm.png"},
        {"country_name": "Japan", "country_code": "jp", "country_image": "https://flagcdn.com/w80/jp.png"},
        {"country_name": "Jordan", "country_code": "jo", "country_image": "https://flagcdn.com/w80/jo.png"},
        {"country_name": "Kazakhstan", "country_code": "kz", "country_image": "https://flagcdn.com/w80/kz.png"},
        {"country_name": "Kenya", "country_code": "ke", "country_image": "https://flagcdn.com/w80/ke.png"},
        {"country_name": "Kiribati", "country_code": "ki", "country_image": "https://flagcdn.com/w80/ki.png"},
        {"country_name": "Korea, North", "country_code": "kp", "country_image": "https://flagcdn.com/w80/kp.png"},
        {"country_name": "Korea, South", "country_code": "kr", "country_image": "https://flagcdn.com/w80/kr.png"},
        {"country_name": "Kosovo", "country_code": "xk", "country_image": "https://flagcdn.com/w80/xk.png"},
        {"country_name": "Kuwait", "country_code": "kw", "country_image": "https://flagcdn.com/w80/kw.png"},
        {"country_name": "Kyrgyzstan", "country_code": "kg", "country_image": "https://flagcdn.com/w80/kg.png"},
        {"country_name": "Laos", "country_code": "la", "country_image": "https://flagcdn.com/w80/la.png"},
        {"country_name": "Latvia", "country_code": "lv", "country_image": "https://flagcdn.com/w80/lv.png"},
        {"country_name": "Lebanon", "country_code": "lb", "country_image": "https://flagcdn.com/w80/lb.png"},
        {"country_name": "Lesotho", "country_code": "ls", "country_image": "https://flagcdn.com/w80/ls.png"},
        {"country_name": "Liberia", "country_code": "lr", "country_image": "https://flagcdn.com/w80/lr.png"},
        {"country_name": "Libya", "country_code": "ly", "country_image": "https://flagcdn.com/w80/ly.png"},
        {"country_name": "Liechtenstein", "country_code": "li", "country_image": "https://flagcdn.com/w80/li.png"},
        {"country_name": "Lithuania", "country_code": "lt", "country_image": "https://flagcdn.com/w80/lt.png"},
        {"country_name": "Luxembourg", "country_code": "lu", "country_image": "https://flagcdn.com/w80/lu.png"},
        {"country_name": "Madagascar", "country_code": "mg", "country_image": "https://flagcdn.com/w80/mg.png"},
        {"country_name": "Malawi", "country_code": "mw", "country_image": "https://flagcdn.com/w80/mw.png"},
        {"country_name": "Malaysia", "country_code": "my", "country_image": "https://flagcdn.com/w80/my.png"},
        {"country_name": "Maldives", "country_code": "mv", "country_image": "https://flagcdn.com/w80/mv.png"},
        {"country_name": "Mali", "country_code": "ml", "country_image": "https://flagcdn.com/w80/ml.png"},
        {"country_name": "Malta", "country_code": "mt", "country_image": "https://flagcdn.com/w80/mt.png"},
        {"country_name": "Marshall Islands", "country_code": "mh", "country_image": "https://flagcdn.com/w80/mh.png"},
        {"country_name": "Mauritania", "country_code": "mr", "country_image": "https://flagcdn.com/w80/mr.png"},
        {"country_name": "Mauritius", "country_code": "mu", "country_image": "https://flagcdn.com/w80/mu.png"},
        {"country_name": "Mexico", "country_code": "mx", "country_image": "https://flagcdn.com/w80/mx.png"},
        {"country_name": "Micronesia", "country_code": "fm", "country_image": "https://flagcdn.com/w80/fm.png"},
        {"country_name": "Moldova", "country_code": "md", "country_image": "https://flagcdn.com/w80/md.png"},
        {"country_name": "Monaco", "country_code": "mc", "country_image": "https://flagcdn.com/w80/mc.png"},
        {"country_name": "Mongolia", "country_code": "mn", "country_image": "https://flagcdn.com/w80/mn.png"},
        {"country_name": "Montenegro", "country_code": "me", "country_image": "https://flagcdn.com/w80/me.png"},
        {"country_name": "Morocco", "country_code": "ma", "country_image": "https://flagcdn.com/w80/ma.png"},
        {"country_name": "Mozambique", "country_code": "mz", "country_image": "https://flagcdn.com/w80/mz.png"},
        {"country_name": "Myanmar", "country_code": "mm", "country_image": "https://flagcdn.com/w80/mm.png"},
        {"country_name": "Namibia", "country_code": "na", "country_image": "https://flagcdn.com/w80/na.png"},
        {"country_name": "Nauru", "country_code": "nr", "country_image": "https://flagcdn.com/w80/nr.png"},
        {"country_name": "Nepal", "country_code": "np", "country_image": "https://flagcdn.com/w80/np.png"},
        {"country_name": "Netherlands", "country_code": "nl", "country_image": "https://flagcdn.com/w80/nl.png"},
        {"country_name": "New Zealand", "country_code": "nz", "country_image": "https://flagcdn.com/w80/nz.png"},
        {"country_name": "Nicaragua", "country_code": "ni", "country_image": "https://flagcdn.com/w80/ni.png"},
        {"country_name": "Niger", "country_code": "ne", "country_image": "https://flagcdn.com/w80/ne.png"},
        {"country_name": "Nigeria", "country_code": "ng", "country_image": "https://flagcdn.com/w80/ng.png"},
        {"country_name": "North Macedonia", "country_code": "mk", "country_image": "https://flagcdn.com/w80/mk.png"},
        {"country_name": "Norway", "country_code": "no", "country_image": "https://flagcdn.com/w80/no.png"},
        {"country_name": "Oman", "country_code": "om", "country_image": "https://flagcdn.com/w80/om.png"},
        {"country_name": "Pakistan", "country_code": "pk", "country_image": "https://flagcdn.com/w80/pk.png"},
        {"country_name": "Palau", "country_code": "pw", "country_image": "https://flagcdn.com/w80/pw.png"},
        {"country_name": "Panama", "country_code": "pa", "country_image": "https://flagcdn.com/w80/pa.png"},
        {"country_name": "Papua New Guinea", "country_code": "pg", "country_image": "https://flagcdn.com/w80/pg.png"},
        {"country_name": "Paraguay", "country_code": "py", "country_image": "https://flagcdn.com/w80/py.png"},
        {"country_name": "Peru", "country_code": "pe", "country_image": "https://flagcdn.com/w80/pe.png"},
        {"country_name": "Philippines", "country_code": "ph", "country_image": "https://flagcdn.com/w80/ph.png"},
        {"country_name": "Poland", "country_code": "pl", "country_image": "https://flagcdn.com/w80/pl.png"},
        {"country_name": "Portugal", "country_code": "pt", "country_image": "https://flagcdn.com/w80/pt.png"},
        {"country_name": "Qatar", "country_code": "qa", "country_image": "https://flagcdn.com/w80/qa.png"},
        {"country_name": "Romania", "country_code": "ro", "country_image": "https://flagcdn.com/w80/ro.png"},
        {"country_name": "Russia", "country_code": "ru", "country_image": "https://flagcdn.com/w80/ru.png"},
        {"country_name": "Rwanda", "country_code": "rw", "country_image": "https://flagcdn.com/w80/rw.png"},
        {"country_name": "Saint Kitts and Nevis", "country_code": "kn", "country_image": "https://flagcdn.com/w80/kn.png"},
        {"country_name": "Saint Lucia", "country_code": "lc", "country_image": "https://flagcdn.com/w80/lc.png"},
        {"country_name": "Saint Vincent and the Grenadines", "country_code": "vc", "country_image": "https://flagcdn.com/w80/vc.png"},
        {"country_name": "Samoa", "country_code": "ws", "country_image": "https://flagcdn.com/w80/ws.png"},
        {"country_name": "San Marino", "country_code": "sm", "country_image": "https://flagcdn.com/w80/sm.png"},
        {"country_name": "Sao Tome and Principe", "country_code": "st", "country_image": "https://flagcdn.com/w80/st.png"},
        {"country_name": "Saudi Arabia", "country_code": "sa", "country_image": "https://flagcdn.com/w80/sa.png"},
        {"country_name": "Senegal", "country_code": "sn", "country_image": "https://flagcdn.com/w80/sn.png"},
        {"country_name": "Serbia", "country_code": "rs", "country_image": "https://flagcdn.com/w80/rs.png"},
        {"country_name": "Seychelles", "country_code": "sc", "country_image": "https://flagcdn.com/w80/sc.png"},
        {"country_name": "Sierra Leone", "country_code": "sl", "country_image": "https://flagcdn.com/w80/sl.png"},
        {"country_name": "Singapore", "country_code": "sg", "country_image": "https://flagcdn.com/w80/sg.png"},
        {"country_name": "Slovakia", "country_code": "sk", "country_image": "https://flagcdn.com/w80/sk.png"},
        {"country_name": "Slovenia", "country_code": "si", "country_image": "https://flagcdn.com/w80/si.png"},
        {"country_name": "Solomon Islands", "country_code": "sb", "country_image": "https://flagcdn.com/w80/sb.png"},
        {"country_name": "Somalia", "country_code": "so", "country_image": "https://flagcdn.com/w80/so.png"},
        {"country_name": "South Africa", "country_code": "za", "country_image": "https://flagcdn.com/w80/za.png"},
        {"country_name": "South Sudan", "country_code": "ss", "country_image": "https://flagcdn.com/w80/ss.png"},
        {"country_name": "Spain", "country_code": "es", "country_image": "https://flagcdn.com/w80/es.png"},
        {"country_name": "Sri Lanka", "country_code": "lk", "country_image": "https://flagcdn.com/w80/lk.png"},
        {"country_name": "Sudan", "country_code": "sd", "country_image": "https://flagcdn.com/w80/sd.png"},
        {"country_name": "Suriname", "country_code": "sr", "country_image": "https://flagcdn.com/w80/sr.png"},
        {"country_name": "Sweden", "country_code": "se", "country_image": "https://flagcdn.com/w80/se.png"},
        {"country_name": "Switzerland", "country_code": "ch", "country_image": "https://flagcdn.com/w80/ch.png"},
        {"country_name": "Syria", "country_code": "sy", "country_image": "https://flagcdn.com/w80/sy.png"},
        {"country_name": "Taiwan", "country_code": "tw", "country_image": "https://flagcdn.com/w80/tw.png"},
        {"country_name": "Tajikistan", "country_code": "tj", "country_image": "https://flagcdn.com/w80/tj.png"},
        {"country_name": "Tanzania", "country_code": "tz", "country_image": "https://flagcdn.com/w80/tz.png"},
        {"country_name": "Thailand", "country_code": "th", "country_image": "https://flagcdn.com/w80/th.png"},
        {"country_name": "Timor-Leste", "country_code": "tl", "country_image": "https://flagcdn.com/w80/tl.png"},
        {"country_name": "Togo", "country_code": "tg", "country_image": "https://flagcdn.com/w80/tg.png"},
        {"country_name": "Tonga", "country_code": "to", "country_image": "https://flagcdn.com/w80/to.png"},
        {"country_name": "Trinidad and Tobago", "country_code": "tt", "country_image": "https://flagcdn.com/w80/tt.png"},
        {"country_name": "Tunisia", "country_code": "tn", "country_image": "https://flagcdn.com/w80/tn.png"},
        {"country_name": "Turkey", "country_code": "tr", "country_image": "https://flagcdn.com/w80/tr.png"},
        {"country_name": "Turkmenistan", "country_code": "tm", "country_image": "https://flagcdn.com/w80/tm.png"},
        {"country_name": "Tuvalu", "country_code": "tv", "country_image": "https://flagcdn.com/w80/tv.png"},
        {"country_name": "Uganda", "country_code": "ug", "country_image": "https://flagcdn.com/w80/ug.png"},
        {"country_name": "Ukraine", "country_code": "ua", "country_image": "https://flagcdn.com/w80/ua.png"},
        {"country_name": "United Arab Emirates", "country_code": "ae", "country_image": "https://flagcdn.com/w80/ae.png"},
        {"country_name": "United Kingdom", "country_code": "gb", "country_image": "https://flagcdn.com/w80/gb.png"},
        {"country_name": "United States", "country_code": "us", "country_image": "https://flagcdn.com/w80/us.png"},
        {"country_name": "Uruguay", "country_code": "uy", "country_image": "https://flagcdn.com/w80/uy.png"},
        {"country_name": "Uzbekistan", "country_code": "uz", "country_image": "https://flagcdn.com/w80/uz.png"},
        {"country_name": "Vanuatu", "country_code": "vu", "country_image": "https://flagcdn.com/w80/vu.png"},
        {"country_name": "Vatican City", "country_code": "va", "country_image": "https://flagcdn.com/w80/va.png"},
        {"country_name": "Venezuela", "country_code": "ve", "country_image": "https://flagcdn.com/w80/ve.png"},
        {"country_name": "Vietnam", "country_code": "vn", "country_image": "https://flagcdn.com/w80/vn.png"},
        {"country_name": "Yemen", "country_code": "ye", "country_image": "https://flagcdn.com/w80/ye.png"},
        {"country_name": "Zambia", "country_code": "zm", "country_image": "https://flagcdn.com/w80/zm.png"},
        {"country_name": "Zimbabwe", "country_code": "zw", "country_image": "https://flagcdn.com/w80/zw.png"},
    ]


    def seed_countries():
        for data in country_data:
            country = Country(**data)
            db.session.add(country)

        db.session.commit()

    user_data = [
        {"username": "john123", "password": "password123", "email": "john@example.com"},
        {"username": "emma456", "password": "password456", "email": "emma@example.com"},
        {"username": "alex789", "password": "password789", "email": "alex@example.com"},
    ]

    # Function to seed users
    def seed_users():
        for data in user_data:
            user = User(**data)
            db.session.add(user)

        db.session.commit()
    
    # List of trip data
    trip_data = [
        {"user_id": 1, "country_id": 10, "date_visited": date(2022, 5, 10)},
        {"user_id": 1, "country_id": 27, "date_visited": date(2022, 7, 22)},
        {"user_id": 2, "country_id": 5, "date_visited": date(2023, 1, 5)},
        {"user_id": 3, "country_id": 45, "date_visited": date(2023, 3, 18)},
    ]

    # Function to seed trips
    def seed_trips():
        for data in trip_data:
            trip = Trip(**data)
            db.session.add(trip)

        db.session.commit()

    # Main seeding function
    def seed():
        seed_countries()
        seed_users()
        seed_trips()

    # Run the seeding function
    seed()
    print("🌱 Countries, Users, and Trips successfully seeded! 🌱")