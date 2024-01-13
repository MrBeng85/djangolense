import {
  ColorTags,
  GradientText,
  Project,
  Section,
  Tags,
} from 'astro-boilerplate-components';

const ProjectList = () => (
  <Section
    title={
      <>
        Projet <GradientText>Récent</GradientText>
      </>
    }
  >
    <div className="flex flex-col gap-6">
      <Project
        name="DjangoLens"
        description="
        Explorez dès maintenant DjangoLens, la plateforme que j'ai créée avec Django, alliant simplicité et robustesse. 
        Cliquez sur l'image pour découvrir comment mes compétences en développement peuvent faire la différence !
        "
        link="https://www.elie-garcia.com"
        img={{
          src: '/assets/images/project-web-backend.png',
          alt: 'Projet Web Backend',
        }}
        category={
          <>
            <Tags color={ColorTags.FUCHSIA}>Python</Tags>
            <Tags color={ColorTags.LIME}>Django</Tags>
            <Tags color={ColorTags.SKY}>HTML / CSS</Tags>
            <Tags color={ColorTags.ROSE}>Pythonanywhere</Tags>
          </>
        }
      />
    </div>
  </Section>
);

export { ProjectList };
