import { Heart } from "lucide-react";
import { Aurora } from "@/components/Aurora";
import { wedding } from "./data";
import { Reveal, Ornament } from "./Reveal";

export function Footer() {
  return (
    <footer className="bg-emerald-ink relative overflow-hidden px-5 pt-20 pb-10">
      <div
        className="pointer-events-none absolute inset-0 opacity-25"
        style={{
          backgroundImage: "url('/images/mandala-texture.jpg')",
          backgroundSize: "120%",
          backgroundPosition: "top center",
        }}
      />
      <Aurora intensity={0.5} />
      <div className="from-emerald-ink/70 via-emerald-ink/85 to-emerald-ink absolute inset-0 bg-gradient-to-b" />

      <img
        src="/images/floral-corner.png"
        alt=""
        aria-hidden
        loading="lazy"
        className="pointer-events-none absolute -top-4 -left-8 w-36 opacity-30"
      />
      <img
        src="/images/floral-corner.png"
        alt=""
        aria-hidden
        loading="lazy"
        className="pointer-events-none absolute -top-4 -right-8 w-36 -scale-x-100 opacity-30"
      />

      <div className="relative mx-auto max-w-md text-center">
        <Reveal>
          <Ornament label="With love" />
          <p className="font-script text-gold-foil mt-6 text-4xl leading-snug">
            Come bless our new beginning
          </p>
          <p className="text-ivory/70 mx-auto mt-5 max-w-sm text-sm leading-relaxed">
            Your presence is the greatest blessing as we celebrate our engagement. Join us
            with your warm smiles, laughter, and best wishes as we step into this joyous journey.
          </p>
        </Reveal>

        <Reveal delay={0.12}>
          <div className="mt-9 flex flex-col items-center">
            <span className="rule-gold w-28" />
            <p className="text-ivory font-display mt-6 text-3xl font-light">
              {wedding.bride.name} <span className="font-script text-gold">&amp;</span>{" "}
              {wedding.groom.name}
            </p>
            <p className="text-ivory/50 mt-2 text-[0.6rem] tracking-[0.4em] uppercase">
              21 · 09 · 2026 · Shivamogga
            </p>
          </div>
        </Reveal>

        <p className="text-ivory/35 mt-12 flex items-center justify-center gap-1.5 text-[0.6rem] tracking-[0.3em] uppercase">
          Made with <Heart className="text-gold h-3 w-3 fill-current" /> for our people
        </p>
      </div>
            <a
          href="https://www.instagram.com/invitestory.in/"
          target="_blank"
          rel="noreferrer"
          className="mt-3 inline-block text-[10px] uppercase tracking-[0.35em] text-current opacity-70 transition-opacity hover:opacity-100"
        >
          Follow @invitestory.in on Instagram
        </a>
      </footer>

  );
}
