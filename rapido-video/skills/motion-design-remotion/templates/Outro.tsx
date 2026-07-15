/** Gabarit OUTRO (CTA) — site + réseaux, aux couleurs de la marque. */
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {z} from 'zod';
import {brandSchema, SAFE, MIN, clampFont, ApercuWatermark} from './_shared';

export const outroSchema = brandSchema.extend({
  cta: z.string().default('Découvrez-en plus'),
  site: z.string().default('votre-site.com'),
  reseaux: z.string().default('@votremarque'),
});

export const Outro: React.FC<z.infer<typeof outroSchema>> = (b) => {
  const frame = useCurrentFrame();
  const up = interpolate(frame, [0, 20], [60, 0], {extrapolateRight: 'clamp'});
  const op = interpolate(frame, [0, 20], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <AbsoluteFill style={{backgroundColor: b.primary, fontFamily: b.fontFamily,
      justifyContent: 'center', alignItems: 'center',
      paddingLeft: SAFE.side, paddingRight: SAFE.side,
      paddingTop: SAFE.top, paddingBottom: SAFE.bottom}}>
      <div style={{transform: `translateY(${up}px)`, opacity: op, textAlign: 'center', color: b.textColor}}>
        <div style={{fontSize: clampFont(64, MIN.title), fontWeight: 900}}>{b.cta}</div>
        <div style={{marginTop: 40, fontSize: clampFont(40, MIN.body), fontWeight: 700}}>{b.site}</div>
        <div style={{marginTop: 16, fontSize: clampFont(36, MIN.body), opacity: 0.9}}>{b.reseaux}</div>
      </div>
      <ApercuWatermark show={b.licence === 'apercu'} />
    </AbsoluteFill>
  );
};
