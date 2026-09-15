import { motion } from "framer-motion";
import { useMemo } from "react";

type PetalsProps = {
  count?: number;
  /** Burst petals fall once and faster (used for tap celebrations). */
  burst?: boolean;
};

/**
 * Drifting flower petals. Pure DOM + Motion so it stays cheap on mobile.
 */
export function Petals({ count = 14, burst = false }: PetalsProps) {
  const petals = useMemo(
    () =>
      Array.from({ length: count }, (_, i) => ({
        id: i,
        left: Math.random() * 100,
        size: 8 + Math.random() * 12,
        delay: burst ? Math.random() * 0.4 : Math.random() * 12,
        duration: (burst ? 3.2 : 11) + Math.random() * 6,
        drift: (Math.random() - 0.5) * 140,
        spin: 180 + Math.random() * 540,
        hue: Math.random() > 0.5 ? "oklch(0.78 0.115 85)" : "oklch(0.62 0.13 18)",
        opacity: 0.35 + Math.random() * 0.45,
      })),
    [count, burst],
  );

  return (
    <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden">
      {petals.map((p) => (
        <motion.span
          key={p.id}
          className="absolute top-[-8%]"
          style={{
            left: `${p.left}%`,
            width: p.size,
            height: p.size * 0.62,
            borderRadius: "60% 10% 60% 10%",
            background: p.hue,
            opacity: p.opacity,
          }}
          initial={{ y: "-10vh", x: 0, rotate: 0 }}
          animate={{ y: "115vh", x: p.drift, rotate: p.spin }}
          transition={{
            duration: p.duration,
            delay: p.delay,
            repeat: burst ? 0 : Infinity,
            ease: "linear",
          }}
        />
      ))}
    </div>
  );
}

export default Petals;
