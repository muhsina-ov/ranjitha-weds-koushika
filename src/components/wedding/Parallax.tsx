import { motion, useScroll, useTransform, useSpring } from "framer-motion";
import { useRef, type ReactNode } from "react";

/**
 * Scroll-linked parallax wrapper. `speed` > 0 moves slower than scroll
 * (drifts down), < 0 moves faster (drifts up).
 */
export function Parallax({
  children,
  speed = 40,
  scaleRange,
  className = "",
}: {
  children: ReactNode;
  speed?: number;
  scaleRange?: [number, number];
  className?: string;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"],
  });
  const smooth = useSpring(scrollYProgress, {
    stiffness: 90,
    damping: 22,
    mass: 0.4,
  });
  const y = useTransform(smooth, [0, 1], [speed, -speed]);
  const scale = useTransform(smooth, [0, 0.5, 1], [
    scaleRange?.[0] ?? 1,
    scaleRange?.[1] ?? 1,
    scaleRange?.[0] ?? 1,
  ]);

  return (
    <div ref={ref} className={className}>
      <motion.div style={{ y, scale }}>{children}</motion.div>
    </div>
  );
}

export default Parallax;
