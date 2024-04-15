import LogoIcon from "../assets/logo.png";

interface FeatureProps {                                                      image: string;                                                            }                                                                                                                                                       const features: FeatureProps[] = [                                            {                                                                             image: LogoIcon,                                                          },                                                                        ];

export const Footer = () => {
  return (
    <footer id="footer">
      <hr className="w-11/12 mx-auto" />

      <section className="container py-20 grid grid-cols-2 md:grid-cols-4 xl:grid-cols-6 gap-x-12 gap-y-8">
        <div className="col-span-full xl:col-span-2">
          <a
            href="/"
            className="font-bold text-xl flex"
          >
             {features.map(({ image }: FeatureProps) => (

              <img
                src={image}
                alt="About feature"
                className="w-[18px] lg:w-[28px] mx-2"
              />
        ))}    DocVerifyRAG
          </a>
        </div>

        <div className="flex flex-col gap-2">
          <h3 className="font-bold text-lg">About Us</h3>
        
<div>
            <a
              href="#"
              className="opacity-60 hover:opacity-100"
            >
              GitHub
            </a>
          </div>
</div>
       <div className="flex flex-col gap-2">
          <h3 className="font-bold text-lg">Industries</h3>

<div>
            <a
              href="#"
              className="opacity-60 hover:opacity-100"
            >
              Health
            </a>
          </div>
<div>
            <a
              href="#"
              className="opacity-60 hover:opacity-100"
            >
              FinTech
            </a>
          </div>
<div>
            <a
              href="#"
              className="opacity-60 hover:opacity-100"
            >
              Banking
            </a>
          </div>
</div>
        <div className="flex flex-col gap-2">
          <h3 className="font-bold text-lg">Follow Us</h3>
          <div>
            <a
              href="#"
              className="opacity-60 hover:opacity-100"
            >
              GitHub
            </a>
          </div>

        
</div>
      </section>

      <section className="container pb-14 text-center">
        <h3>
          &copy; 2024 Efficient Document Verification by{" "}
          <a
            target="_blank"
            href="https://github.com/eliawaefler/DocVerifyRAG"
            className="text-primary transition-all border-primary hover:border-b-2"
          >
            DocVerifyRAG
          </a>
        </h3>
      </section>
    </footer>
  );
};
