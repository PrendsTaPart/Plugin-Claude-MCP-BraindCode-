/**
 * Registre des compositions (Remotion). 1080x1920 @ 30 fps par défaut.
 * Le skill motion-design-remotion copie ce dossier `templates/` dans le projet
 * Remotion créé au workspace, puis rend la composition voulue via la CLI Remotion
 * avec les props de marque (defaultProps surchargés en ligne de commande).
 */
import {Composition} from 'remotion';
import {Intro, introSchema} from './Intro';
import {Outro, outroSchema} from './Outro';
import {LowerThird, lowerThirdSchema} from './LowerThird';
import {TitleCard, titleCardSchema} from './TitleCard';
import {StatBar, statBarSchema} from './StatBar';

const W = 1080, H = 1920, FPS = 30;

export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="Intro" component={Intro} schema={introSchema}
      durationInFrames={4 * FPS} fps={FPS} width={W} height={H}
      defaultProps={introSchema.parse({})} />
    <Composition id="Outro" component={Outro} schema={outroSchema}
      durationInFrames={5 * FPS} fps={FPS} width={W} height={H}
      defaultProps={outroSchema.parse({})} />
    <Composition id="LowerThird" component={LowerThird} schema={lowerThirdSchema}
      durationInFrames={5 * FPS} fps={FPS} width={W} height={H}
      defaultProps={lowerThirdSchema.parse({})} />
    <Composition id="TitleCard" component={TitleCard} schema={titleCardSchema}
      durationInFrames={4 * FPS} fps={FPS} width={W} height={H}
      defaultProps={titleCardSchema.parse({})} />
    <Composition id="StatBar" component={StatBar} schema={statBarSchema}
      durationInFrames={3 * FPS} fps={FPS} width={W} height={H}
      defaultProps={statBarSchema.parse({})} />
  </>
);
