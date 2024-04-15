import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { MedalIcon, MapIcon, PlaneIcon } from "../components/Icons";

interface FeatureProps {
  icon: JSX.Element;
  title: string;
  description: string;
}

const features: FeatureProps[] = [
  {
    icon: <MedalIcon />,
    title: "Document Classification",
    description:    "Utilizes AI/ML algorithms to classify documents based on content and metadata",  },
  {
    icon: <MapIcon />,
    title: "Anomaly Detection",
    description:
      "Identifies mistakes and misclassifications in document metadata through automated anomaly detection",
  },
  {
    icon: <PlaneIcon />,
    title: "User-Friendly Interface",
    description:
      "Simplifies the document management process for hospital staff, reducing manual effort and errors",
  },
];

export const HowItWorks = () => {
  return (
    <section
      id="howItWorks"
      className="container text-center py-22 sm:py-30"
    >
      <h2 className="text-3xl md:text-4xl font-bold ">
        Fast and Accurate{" "}
        <span className="bg-gradient-to-b from-primary/60 to-primary text-transparent bg-clip-text">
          Document Meta Data{" "}
        </span>
       Verification
      </h2>
      <p className="md:w-3/4 mx-auto mt-4 mb-8 text-xl text-muted-foreground">
        DocVerifyRAG revolutionizes document verification in healthcare, harnessing AI to classify documents and rectify metadata errors. With automated anomaly detection, ensure precise data management, compliance, and enhanced patient care.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {features.map(({ icon, title, description }: FeatureProps) => (
          <Card
            key={title}
            className="bg-muted/50"
          >
            <CardHeader>
              <CardTitle className="grid gap-4 place-items-center">
                {icon}
                {title}
              </CardTitle>
            </CardHeader>
            <CardContent>{description}</CardContent>
          </Card>
        ))}
      </div>
    </section>
  );
};
