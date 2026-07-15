/** Gabarit LOWER-THIRD — nom + fonction (bandeau bas, hors safe zone). */
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {z} from 'zod';
import {brandSchema, SAFE, MIN, clampFont, ApercuWatermark} from './_shared';

export const lowerThirdSchema = brandSchema.extend({
  nom: z.string().default('Prénom Nom'),
  fonction: z.string().default('Fonction'),
});

export const LowerThird: React.FC<z.infer<typeof lowerThirdSchema>> = (b) => {
  const frame = useCurrentFrame();
  const slide = interpolate(frame, [0, 15], [-600, 0], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{fontFamily: b.fontFamily}}>
      <div style={{position: 'absolute', left: SAFE.side, bottom: SAFE.bottom + 40,
        transform: `translateX(${slide}px)`,
        background: b.primary, padding: '20px 32px', borderRadius: 12,
        borderLeft: `10px solid ${b.textColor}`}}>
        <div style={{color: b.textColor, fontSize: clampFont(48, MIN.body), fontWeight: 800}}>{b.nom}</div>
        <div style={{color: b.textColor, fontSize: clampFont(34, MIN.floor), opacity: 0.9, marginTop: 6}}>
          {b.fonction}
        </div>
      </div>
      <ApercuWatermark show={b.licence === 'apercu'} />
    </AbsoluteFill>
  );
};
