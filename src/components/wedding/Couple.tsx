import { wedding } from "./data";
import { Parallax } from "./Parallax";
import { Reveal, Ornament } from "./Reveal";

function Person({ person, role }: { person: typeof wedding.bride; role: string }) {
  return (
    <Reveal className="relative">
      <div className="bg-card/70 border-gold/30 shadow-luxe relative overflow-hidden rounded-[2rem] border p-6 backdrop-blur-sm">
        <div
          className="pointer-events-none absolute inset-0 opacity-[0.07]"
          style={{
            backgroundImage: "url('/images/mandala-texture.jpg')",
            backgroundSize: "cover",
          }}
        />
        <div className="relative flex flex-col items-center text-center">
          <div className="from-gold/25 relative h-40 w-40 overflow-hidden rounded-full bg-gradient-to-b to-transparent shadow-inner">
            <img
              src={person.image}
              alt={person.fullName}
              loading="lazy"
              width={768}
              height={896}
              className="h-full w-full object-cover object-center"
            />
          </div>
          <span className="text-gold mt-5 text-[0.6rem] tracking-[0.45em] uppercase">{role}</span>
          <h3 className="text-primary mt-2 text-3xl font-light">{person.fullName}</h3>
          <p className="text-muted-foreground mt-1 text-xs tracking-wide">{person.line}</p>
          <span className="rule-gold my-4 w-20" />
          <p className="text-foreground/75 text-sm leading-relaxed">{person.note}</p>
        </div>
      </div>
    </Reveal>
  );
}

export function Couple() {
  return (
    <section className="relative overflow-hidden px-5 py-20">
      <img
        src="/images/floral-corner.png"
        alt=""
        aria-hidden
        loading="lazy"
        className="pointer-events-none absolute -top-6 -left-10 w-44 opacity-40"
      />
      <img
        src="/images/floral-corner.png"
        alt=""
        aria-hidden
        loading="lazy"
        className="pointer-events-none absolute -right-10 -bottom-6 w-44 rotate-180 opacity-40"
      />

      <div className="relative mx-auto max-w-md">
        <Reveal className="text-center">
          <Ornament label="The Couple" />
          <h2 className="text-primary mt-5 text-4xl font-light">Two hearts, one promise</h2>
          <p className="text-muted-foreground mx-auto mt-3 max-w-xs text-sm leading-relaxed">
            As we celebrate our engagement, we invite you to be part of our joy, traditions, and new
            beginnings.
          </p>
        </Reveal>

        <div className="mt-10 space-y-8">
          <Parallax speed={26}>
            <Person person={wedding.bride} role="The Bride" />
          </Parallax>
          <div className="flex justify-center">
            <span className="font-script text-gold animate-float-soft text-5xl">&amp;</span>
          </div>
          <Parallax speed={-26}>
            <Person person={wedding.groom} role="The Groom" />
          </Parallax>
        </div>
      </div>
    </section>
  );
}
