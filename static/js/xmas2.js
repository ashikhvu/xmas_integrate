/**
 * Creates a Mo.js party popper animation.
 *
 * @property {string}  selector - DOM selector to attach the animation to
 * @property {boolean} [debug]  - If enabled, add a debug timeline
 */

function partyPopper(selector, debug) {
	const colors = ["#bea4ff", "#feb535", "#ff6e83", "#58cafe"];

	const flight = {
		isSwirl: true,
		swirlSize: "rand(10, 20)",
		swirlFrequency: "rand(1, 3)",
		direction: [-1, 1],
		degreeShift: "rand(-15, 15)",
		duration: 1200,
		easing: "cubic.out",
		pathScale: "stagger(.2)"
	};

	// Confetti shapes
	const torsade = {
		shape: "zigzag",
		points: "rand(4, 6)",
		radius: 40,
		radiusY: 30,
		strokeLinecap: "round",
		strokeWidth: 8,
		fill: "none",
		stroke: colors,
		angle: { 0: "rand(-720, 720)" },
		...flight
	};

	const bent = {
		shape: "curve",
		radius: "rand(25, 35)",
		radiusY: 15,
		strokeLinecap: "round",
		strokeWidth: 8,
		fill: "none",
		stroke: colors,
		angle: { 0: "rand(-720, 720)" },
		...flight
	};

	const flake = {
		shape: "circle",
		radius: "rand(5, 10)",
		fill: colors,
		...flight
	};

	// Bursts
	const burst = {
		parent: selector,
		radius: { 0: "rand(50, 100)" },
		count: "rand(18, 22)",
		degree: 30
	};

	const torsadeBurst = new mojs.Burst({
		...burst,
		children: {
			...torsade
		}
	});

	const bentBurst = new mojs.Burst({
		...burst,
		children: {
			...bent
		}
	});

	const flakeBurst = new mojs.Burst({
		...burst,
		children: {
			...flake
		}
	});

	// Timeline (debug only)
	if (debug != null) {
		const timeline = new mojs.Timeline();

		timeline.add(torsadeBurst, bentBurst, flakeBurst);

		new MojsPlayer({
			add: timeline,
			isPlaying: true,
			isRepeat: true
		});
	} else {
		torsadeBurst.play();
		bentBurst.play();
		flakeBurst.play();
	}
}

partyPopper(".party-popper", true);