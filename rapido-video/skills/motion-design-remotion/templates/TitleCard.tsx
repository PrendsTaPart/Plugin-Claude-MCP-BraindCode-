/** Gabarit ÉCRAN TITRE — grand titre centré + sous-titre optionnel. */
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {brandSchema, SAFE, MIN, clampFont, ApercuWatermark} from './_shared';

export const titleCardSchema = brandSchema.extend({
  titre: z.string().default('Titre de la séquence'),
  sousTitre: z.string().default(''),
});

export const TitleCard: React.FC<z.infer<typeof titleCardSchema>> = (b) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const s = spring({frame, fps, config: {damping: 200}});
  const barW = interpolate(s, [0, 1], [0, 320]);
  return (
    <AbsoluteFill style={{backgroundColor: b.secondary, fontFamily: b.fontFamily,
      justifyContent: 'center', alignItems: 'center',
      paddingLeft: SAFE.side, paddingRight: SAFE.side}}>
      <div style={{width: barW, height: 10, background: b.primary, borderRadius: 6, marginBottom: 32}} />
      <div style={{color: b.textColor, fontSize: clampFont(72, MIN.title), fontWeight: 900,
        textAlign: 'center', opacity: s}}>{b.titre}</div>
      {b.sousTitre ? (
        <div style={{color: b.textColor, opacity: 0.85 * s, marginTop: 20,
          fontSize: clampFont(38, MIN.body), textAlign: 'center'}}>{b.sousTitre}</div>
      ) : null}
      <ApercuWatermark show={b.licence === 'apercu'} />
    </AbsoluteFill>
  );
};
