import { CalendarPlus, Clock, MapPin, Navigation, Sparkles } from "lucide-react";
import { motion } from "framer-motion";
import { wedding } from "./data";
import { Reveal, Ornament } from "./Reveal";

function icsStamp(iso: string) {
  return new Date(iso).toISOString().replace(/[-:]/g, "").split(".")[0] + "Z";
}

function addToCalendar() {
  const ics = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//Engagement Invite//EN",
    "BEGIN:VEVENT",
    `UID:${Date.now()}@engagement`,
    `DTSTAMP:${icsStamp(new Date().toISOString())}`,
    `DTSTART:${icsStamp(wedding.dateISO)}`,
    `DTEND:${icsStamp(wedding.endISO)}`,
    `SUMMARY:${wedding.bride.name} & ${wedding.groom.name} — Engagement Ceremony`,
    `LOCATION:${wedding.venue.name}, ${wedding.venue.address}`,
    "DESCRIPTION:With love and joy, we invite you to celebrate our engagement.",
    "END:VEVENT",
    "END:VCALENDAR",
  ].join("\r\n");

  const url = URL.createObjectURL(new Blob([ics], { type: "text/calendar" }));
  const a = document.createElement("a");
  a.href = url;
  a.download = "ranjitha-koushik-engagement.ics";
  a.click();
  URL.revokeObjectURL(url);
}

const rows = [
  { icon: Sparkles, label: "The Ceremony", value: wedding.muhurthamLabel },
  { icon: Clock, label: "Time", value: wedding.timeLabel },
  { icon: MapPin, label: "Venue", value: wedding.venue.name },
];

export function EventDetails() {
  return (
    <section className="relative px-5 py-20">
      <div className="mx-auto max-w-md">
        <Reveal className="text-center">
          <Ornament label="When & Where" />
          <h2 className="text-primary mt-5 text-4xl font-light">The celebration</h2>
        </Reveal>

        <Reveal delay={0.1}>
          <div className="border-gold/30 bg-card shadow-luxe mt-8 overflow-hidden rounded-[2rem] border">
            <div className="from-primary to-emerald-ink bg-gradient-to-br px-6 py-7 text-center">
              <p className="text-gold/80 text-[0.6rem] tracking-[0.45em] uppercase">
                Save the date
              </p>
              <p className="text-ivory font-display mt-2 text-5xl font-light">21</p>
              <p className="text-ivory/85 text-sm tracking-[0.35em] uppercase">September 2026</p>
            </div>

            <div className="divide-gold/15 divide-y">
              {rows.map(({ icon: Icon, label, value }) => (
                <div key={label} className="flex items-center gap-4 px-6 py-4">
                  <span className="bg-secondary text-primary grid h-10 w-10 shrink-0 place-items-center rounded-full">
                    <Icon className="h-4 w-4" />
                  </span>
                  <div className="min-w-0">
                    <p className="text-muted-foreground text-[0.6rem] tracking-[0.3em] uppercase">
                      {label}
                    </p>
                    <p className="text-foreground truncate text-sm">{value}</p>
                  </div>
                </div>
              ))}
            </div>

            <div className="px-6 pt-2 pb-6">
              <motion.button
                whileTap={{ scale: 0.97 }}
                onClick={addToCalendar}
                className="from-primary to-emerald-ink text-ivory shadow-gold flex w-full items-center justify-center gap-2 rounded-full bg-gradient-to-r py-4 text-xs tracking-[0.3em] uppercase"
              >
                <CalendarPlus className="h-4 w-4" />
                Add to calendar
              </motion.button>
            </div>
          </div>
        </Reveal>

        <Reveal delay={0.16}>
          <div className="border-gold/30 bg-card shadow-luxe mt-6 overflow-hidden rounded-[2rem] border">
            <div className="relative">
              <img
                src="/images/map-preview.jpg"
                alt={`Map to ${wedding.venue.name}`}
                loading="lazy"
                width={1024}
                height={768}
                className="h-48 w-full object-cover"
              />
              <div className="from-card absolute inset-0 bg-gradient-to-t via-transparent to-transparent" />
            </div>
            <div className="px-6 pt-2 pb-6 text-center">
              <p className="text-primary text-xl">{wedding.venue.name}</p>
              <p className="text-muted-foreground mt-1 text-xs">{wedding.venue.address}</p>
              <motion.a
                whileTap={{ scale: 0.97 }}
                href={wedding.venue.mapUrl}
                target="_blank"
                rel="noreferrer"
                className="border-gold/50 text-primary hover:bg-secondary mt-5 inline-flex items-center justify-center gap-2 rounded-full border px-7 py-3.5 text-xs tracking-[0.3em] uppercase transition-colors"
              >
                <Navigation className="h-4 w-4" />
                Get directions
              </motion.a>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
