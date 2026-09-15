import { AnimatePresence, motion } from "framer-motion";
import { useEffect, useState } from "react";
import { wedding } from "./data";
import { Reveal, Ornament } from "./Reveal";

const TARGET = new Date(wedding.dateISO).getTime();

function diff() {
  const ms = Math.max(0, TARGET - Date.now());
  return {
    days: Math.floor(ms / 86400000),
    hours: Math.floor((ms / 3600000) % 24),
    minutes: Math.floor((ms / 60000) % 60),
    seconds: Math.floor((ms / 1000) % 60),
  };
}

function Unit({ value, label }: { value: number; label: string }) {
  const text = String(value).padStart(2, "0");
  return (
    <div className="border-gold/25 bg-emerald-ink/40 relative flex flex-col items-center overflow-hidden rounded-2xl border px-2 py-4 backdrop-blur-sm">
      <div className="relative h-11 w-full overflow-hidden">
        <AnimatePresence mode="popLayout" initial={false}>
          <motion.span
            key={text}
            initial={{ y: "70%", opacity: 0, filter: "blur(4px)" }}
            animate={{ y: "0%", opacity: 1, filter: "blur(0px)" }}
            exit={{ y: "-70%", opacity: 0, filter: "blur(4px)" }}
            transition={{ duration: 0.45, ease: [0.22, 1, 0.36, 1] }}
            className="text-gold-foil font-display absolute inset-0 flex items-center justify-center text-4xl font-light tabular-nums"
          >
            {text}
          </motion.span>
        </AnimatePresence>
      </div>
      <span className="text-ivory/55 mt-2 text-[0.55rem] tracking-[0.3em] uppercase">
        {label}
      </span>
    </div>
  );
}

export function Countdown() {
  const [t, setT] = useState(diff);

  useEffect(() => {
    const id = setInterval(() => setT(diff()), 1000);
    return () => clearInterval(id);
  }, []);

  return (
    <section className="bg-emerald-ink relative overflow-hidden px-5 py-20">
      <div
        className="pointer-events-none absolute inset-0 opacity-20"
        style={{
          backgroundImage: "url('/images/mandala-texture.jpg')",
          backgroundSize: "140%",
          backgroundPosition: "center",
        }}
      />
      <div className="from-emerald-ink via-emerald-ink/60 to-emerald-ink absolute inset-0 bg-gradient-to-b" />

      <div className="relative mx-auto max-w-md text-center">
        <Reveal>
          <Ornament label="Counting down" />
          <h2 className="text-ivory mt-5 text-4xl font-light">
            Until our <span className="font-script text-gold-foil">engagement</span>
          </h2>
        </Reveal>

        <Reveal delay={0.12}>
          <div className="mt-9 grid grid-cols-4 gap-2.5">
            <Unit value={t.days} label="Days" />
            <Unit value={t.hours} label="Hours" />
            <Unit value={t.minutes} label="Mins" />
            <Unit value={t.seconds} label="Secs" />
          </div>
        </Reveal>

        <Reveal delay={0.2}>
          <p className="text-ivory/55 mt-6 text-xs tracking-[0.25em] uppercase">
            {wedding.dateLabel}
          </p>
        </Reveal>
      </div>
    </section>
  );
}
