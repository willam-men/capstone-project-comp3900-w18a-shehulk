const ProgressBar = (page) => {
  const title = [
    "1. Basics",
    "2. Ingredients",
    "3. Recipe Steps",
    "4. Extra Details",
  ];
  const progress = [0, 20, 46, 73];

  const steps = title.map((i, value) => {
    return <div className="bar"> {title[value]} </div>;
  });

  return (
    <section className="progress-container">
      <div className="barmarker-container">{steps}</div>
      <progress
        className="barmarker"
        max="100"
        value={progress[page.page]}
      ></progress>
    </section>
  );
};

export default ProgressBar;
