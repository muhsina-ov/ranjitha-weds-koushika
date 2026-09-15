type AuroraProps = {
  className?: string;
  /** Extra opacity multiplier for the whole field. */
  intensity?: number;
};

/**
 * Aurora background: layered, slowly drifting colour fields.
 * Pure CSS so it renders on SSR and costs nothing on low-end mobiles.
 */
export function Aurora({ className = "", intensity = 1 }: AuroraProps) {
  return (
    <div
      aria-hidden
      className={`pointer-events-none absolute inset-0 overflow-hidden ${className}`}
      style={{ opacity: intensity }}
    >
      <div
        className="absolute -top-1/3 left-[-20%] h-[80%] w-[90%] rounded-full blur-3xl"
        style={{
          background:
            "radial-gradient(circle at 50% 50%, oklch(0.55 0.13 160 / 0.55), transparent 65%)",
          animation: "aurora-drift 18s ease-in-out infinite",
        }}
      />
      <div
        className="absolute top-[10%] right-[-25%] h-[75%] w-[85%] rounded-full blur-3xl"
        style={{
          background:
            "radial-gradient(circle at 50% 50%, oklch(0.8 0.12 85 / 0.5), transparent 65%)",
          animation: "aurora-drift 24s ease-in-out infinite reverse",
        }}
      />
      <div
        className="absolute bottom-[-25%] left-[10%] h-[70%] w-[80%] rounded-full blur-3xl"
        style={{
          background:
            "radial-gradient(circle at 50% 50%, oklch(0.52 0.16 18 / 0.4), transparent 65%)",
          animation: "aurora-drift 30s ease-in-out infinite",
        }}
      />
      <div
        className="absolute inset-0 mix-blend-soft-light"
        style={{
          backgroundImage:
            "radial-gradient(oklch(0.98 0.02 92 / 0.35) 1px, transparent 1px)",
          backgroundSize: "22px 22px",
        }}
      />
    </div>
  );
}

export default Aurora;
