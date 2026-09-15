import { motion, type Variants } from "framer-motion";
import type { ReactNode } from "react";

const variants: Variants = {
  hidden: { opacity: 0, y: 20 },
  show: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.85, ease: [0.22, 1, 0.36, 1] },
  },
};

export function Reveal({
  children,
  delay = 0,
  className = "",
}: {
  children: ReactNode;
  delay?: number;
  className?: string;
}) {
  return (
    <motion.div
      className={className}
      variants={variants}
      initial="hidden"
      whileInView="show"
      viewport={{ once: true, amount: 0.25 }}
      transition={{ delay }}
    >
      {children}
    </motion.div>
  );
}

export function Ornament({ label }: { label?: string }) {
  return (
    <div className="flex items-center justify-center gap-3">
      <span className="rule-gold w-16" />
      {label ? (
        <span className="font-sans text-[0.65rem] tracking-[0.42em] text-gold uppercase">
          {label}
        </span>
      ) : (
        <span className="text-gold text-sm">✦</span>
      )}
      <span className="rule-gold w-16" />
    </div>
  );
}
